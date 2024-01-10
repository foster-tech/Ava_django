from django.shortcuts import render, get_object_or_404
from datetime import date, datetime
from django.db.models import Count
from .models import Indicador, ProtocoloIndicador, Status, Tarefa, Formulario, TabelaConteudoIndicador, DefinicoesProtocolo, InfoHead, Formulario
import plotly.figure_factory as ff
from django.http import JsonResponse
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def index(request):
    ano_atual = datetime.now().year
    
    indicadores_ano_atual = []
    indicadores_anos_anteriores = []
    
    formularios_ano_atual = []
    formularios_anos_anteriores = []
    
    indicadores = Indicador.objects.all()
    
    for indicador in indicadores:
        if indicador.ano == ano_atual:
            indicadores_ano_atual.append(indicador)
        else:
            indicadores_anos_anteriores.append(indicador)
            
    formularios = Formulario.objects.all()
    
    for formulario in formularios:
        if formulario.ano == ano_atual:
            formularios_ano_atual.append(formulario)
        else:
            formularios_anos_anteriores.append(formulario)
    
    anos_disponiveis = Formulario.objects.values_list('ano', flat=True).distinct()
    
    total_formularios_atual = len(formularios_ano_atual)
    total_indicadores_atual = len(indicadores_ano_atual)
    
    total_formularios_anterior = len(formularios_anos_anteriores)
    total_indicadores_anterior = len(indicadores_anos_anteriores)
    
    
    all_status = Status.objects.all()
    status_count = Formulario.objects.values('status__valor').annotate(count=Count('status__valor'))

    # Cria um dicionário para armazenar a contagem de formulários para cada status
    status_data = {status.valor: 0 for status in all_status}

    # Atualiza o dicionário com a contagem real de formulários
    for item in status_count:
        status_valor = item['status__valor']
        status_data[status_valor] = item['count']

    # Converta os dados em listas para uso no gráfico
    labels = [status.get_valor_display() for status in all_status]
    data = [status_data[status.valor] for status in all_status]
    
    tarefas = Tarefa.objects.all()
    df = []
    
    for tarefa in tarefas:
        data_i = tarefa.data_inicio.strftime('%Y-%m-%d')
        data_f = tarefa.data_fim.strftime('%Y-%m-%d')
        df.append(dict(Task=tarefa.nome, Start=data_i, Finish=data_f)) 
    
    
    # fig = ff.create_gantt(df, index_col=False, title=None, show_hover_fill=False)
    
    # fig.update_layout(
    # margin=dict(l=40, r=20, t=20, b=20),
    # )
    
    # graph_html = fig.to_html(full_html=False, default_height=490, default_width='100%')
    
    context = {
        'selected_ano': ano_atual,
        'indicadores_ano_atual': total_indicadores_atual,
        'formularios_ano_atual': total_formularios_atual,
        'indicadores_anos_anteriores': total_indicadores_anterior,
        'formularios_anos_anteriores': total_formularios_anterior,
        'ano_atual': ano_atual,
        'labelsStatus': labels, 
        'data': data,
        # 'graph_html': graph_html, 
        'anos': anos_disponiveis
        }
    
    return render(request, 'index.html', context=context)

def atualizar_totais(request):
    ano_selecionado = request.GET.get('ano', None)

    total_indicadores = 0
    total_formularios = 0
    total_formularios_pendentes = 0

    if ano_selecionado:
        total_indicadores = Indicador.objects.filter(ano=ano_selecionado).count()
        total_formularios = Formulario.objects.filter(ano=ano_selecionado).count()
        total_formularios_pendentes = Formulario.objects.filter(ano=ano_selecionado).exclude(status__valor='3').count()
    
    # Contagem de formulários por status para o ano selecionado
    status_counts = Formulario.objects.filter(ano=ano_selecionado).values('status__valor').annotate(count=Count('status__valor'))

    # Cria um dicionário para armazenar a contagem de formulários para cada status
    status_data = {status.get_valor_display(): 0 for status in Status.objects.all()}

    # Atualiza o dicionário com a contagem real de formulários
    for item in status_counts:
        status_valor = item['status__valor']
        legenda_status = Status.objects.get(valor=status_valor).get_valor_display()
        status_data[legenda_status] = item['count']

    return JsonResponse({'total_indicadores': total_indicadores, 'total_formularios': total_formularios, 'total_formularios_pendentes': total_formularios_pendentes,'status_data': status_data})


def formularios(request):
    ano_atual = datetime.now().year
    
    formularios = Formulario.objects.all()
    
     # lista para armazenar informações de formulários e indicadores
    dados_formularios = []

    # Para cada formulário, obtenha suas informações e indicadores relacionados
    for formulario in formularios:
        dado_formulario = {
            'formulario': formulario,
            'indicadores': formulario.indicador_set.all()  # Isso assume que o nome do relacionamento é 'indicador_set'
        }
        dados_formularios.append(dado_formulario)

    context = {
        'dados_formularios': dados_formularios,
        'ano_atual': ano_atual,
    }
    
    return render(request, 'formularios.html', context=context)


def indicador(request, formulario_id):
    ano_atual = datetime.now().year
    formulario = get_object_or_404(Formulario, id=formulario_id)
    protocolos = ProtocoloIndicador.objects.filter(formulario=formulario)
    info_head = InfoHead.objects.filter(formulario=formulario)
    
    # Obtém o conteúdo atual relacionado ao formulário e ao ano atual
    conteudo_atual = TabelaConteudoIndicador.objects.filter(formulario=formulario, ano_criacao=date.today().year).first()

    # Obtém o conteúdo anterior relacionado ao formulário, excluindo o ano atual
    conteudo_anterior = TabelaConteudoIndicador.objects.filter(formulario=formulario).exclude(ano_criacao=date.today().year)
    
    # Criar uma lista de definições para cada protocolo
    definicoes_protocolo_lista = []
    for protocolo in protocolos:
        definicoes_protocolo_lista.append({
            'protocolo': protocolo,
            'definicoes': DefinicoesProtocolo.objects.filter(protocolo=protocolo)
        })

    context = {
        'formulario': formulario,
        'protocolos': protocolos,
        'definicoes_protocolo_lista': definicoes_protocolo_lista,
        'info_head': info_head,
        'conteudo_atual': conteudo_atual,
        'conteudo_anterior': conteudo_anterior,
        'ano_atual': ano_atual
    }
    
    
    return render(request, 'indicador.html', context=context)

def consolidado(request):
    ano_atual = datetime.now().year
    ultimos_tres_anos = list(range(ano_atual, ano_atual - 3, -1))
    
    formularios = Formulario.objects.all()
    
    indicadores = Indicador.objects.all()
    protocolos = ProtocoloIndicador.objects.all()

    dados_indicadores = {}

    # Criar um dicionário de protocolos para facilitar a busca
    dict_protocolos = {protocolo.indicador.gri.numero: protocolo.descricao for protocolo in protocolos}

    for indicador in indicadores:
        numero_gri = indicador.gri.numero
        ano = indicador.ano
        tema = indicador.tema

        # Se o GRI ainda não estiver no dicionário, crie uma nova entrada
        if numero_gri not in dados_indicadores:
            dados_indicadores[numero_gri] = {'tema': tema, 'gri': numero_gri, 'anos': [ano], 'protocolo': dict_protocolos.get(numero_gri, '')}
        else:
            # Se o GRI já estiver no dicionário, adicione o ano à lista existente
            dados_indicadores[numero_gri]['anos'].append(ano)
            # Adicione a descrição do protocolo
            dados_indicadores[numero_gri]['protocolo'] = dict_protocolos.get(numero_gri, '')

    
    context = {
        'ultimos_tres_anos': ultimos_tres_anos,
        'formularios': formularios,
        'dados_indicadores': dados_indicadores
    }
    
    return render(request, 'consolidado.html', context=context)

def status(request):
    return render(request, 'status.html')

def comunicados(request):
    return render(request, 'comunicados.html')

def informes(request):
    return render(request, 'informes.html')

def pmo(request):
    return render(request, 'pmo.html')
