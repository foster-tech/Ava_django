from django.shortcuts import render, get_object_or_404
from itertools import zip_longest
from datetime import date, datetime
from django.db.models import Count
from .models import Indicador, GRI, ProtocoloIndicador, Status, Tarefa, Formulario, TabelaConteudoIndicador, DefinicoesProtocolo, InfoHead, Formulario
import plotly.figure_factory as ff
from django.http import JsonResponse
import logging


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

    # Recupera formulários
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
    
    # Obtenha todos os status, mesmo aqueles sem formulários associados
    all_status = Status.objects.all()

    # Obtenha a contagem de formulários para cada status
    status_count = Formulario.objects.values('status__valor').annotate(count=Count('status__valor'))

    # Crie um dicionário para armazenar a contagem de formulários para cada status
    status_data = {status.valor: 0 for status in all_status}

    # Atualize o dicionário com a contagem real de formulários
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
    
    
    
    
    fig = ff.create_gantt(df, index_col=False, title=None, show_hover_fill=False)
    
    fig.update_layout(
    margin=dict(l=40, r=20, t=20, b=20),
    )
    
    graph_html = fig.to_html(full_html=False, default_height=490, default_width='100%')
    
    context = {
        'selected_ano': ano_atual,
        'indicadores_ano_atual': total_indicadores_atual,
        'formularios_ano_atual': total_formularios_atual,
        'indicadores_anos_anteriores': total_indicadores_anterior,
        'formularios_anos_anteriores': total_formularios_anterior,
        'ano_atual': ano_atual,
        'labels': labels, 
        'data': data,
        'graph_html': graph_html, 
        'anos': anos_disponiveis
    }
    
    return render(request, 'index.html', context=context)

def atualizar_totais(request):
    ano_selecionado = request.GET.get('ano', None)

    total_indicadores = 0
    total_formularios = 0

    # E de indicadores e formulários para o ano selecionado
    if ano_selecionado:
        total_indicadores = Indicador.objects.filter(ano=ano_selecionado).count()
        total_formularios = Formulario.objects.filter(ano=ano_selecionado).count()
    
    # Obter todos os status possíveis
    todos_status = Status.objects.all()

    # Crie um dicionário para armazenar a contagem de formulários para cada status
    status_data = {status.get_valor_display(): 0 for status in todos_status}

    # Contagem de formulários por status para o ano selecionado
    status_counts = Formulario.objects.filter(ano=ano_selecionado).values('status__valor').annotate(count=Count('status__valor'))

    # Atualize o dicionário com a contagem real de formulários
    for item in status_counts:
        status_valor = item['status__valor']
        legenda_status = Status.objects.get(valor=status_valor).get_valor_display()
        status_data[legenda_status] = item['count']



    # Retorna os totais como uma resposta JSON
    return JsonResponse({'total_indicadores': total_indicadores, 'total_formularios': total_formularios, 'status_data': status_data})

def formularios(request):
    ano_atual = datetime.now().year
    
    formularios = Formulario.objects.all()
    
     # lista para armazenar informações de formulários e indicadores
    dados_formularios = []

    # Para cada formulário, obtenha suas informações e indicadores relacionados
    for formulario in formularios:
        dados_formulario = {
            'formulario': formulario,
            'indicadores': formulario.indicador_set.all()  # Isso assume que o nome do relacionamento é 'indicador_set'
        }
        dados_formularios.append(dados_formulario)

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

def informes(request):
    return render(request, 'informes.html')

def pmo(request):
    return render(request, 'pmo.html')
