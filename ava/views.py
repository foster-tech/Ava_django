from django.shortcuts import render, get_object_or_404
from django.core import serializers
from datetime import date, datetime
from django.db.models import Count
from .models import Indicador, GRI, ProtocoloGRI, DadosConteudoIndicador, Status, Tarefa
import plotly.figure_factory as ff


def index(request):
    ano_atual = datetime.now().year
    total_indicadores = Indicador.objects.count()
    
    status_counts = Status.objects.annotate(indicador_count=Count('indicador'))
    status_counts_dict = {status.get_valor_display(): status.indicador_count for status in status_counts}
    
    labels = [status[1] for status in Status.STATUS_CHOICES]
    data = [status_counts_dict.get(status[1], 0) for status in Status.STATUS_CHOICES]
    
    tarefas = Tarefa.objects.all()
    df = []
    
    for tarefa in tarefas:
        data_i = tarefa.data_inicio.strftime('%Y-%m-%d')
        data_f = tarefa.data_fim.strftime('%Y-%m-%d')
        df.append(dict(Task=tarefa.nome, Start=data_i, Finish=data_f)) 
    
    
    
    
    fig = ff.create_gantt(df, index_col=None)
    
    fig.update_layout(
    xaxis_title='Datas',
    yaxis_title='Tarefas',
    margin=dict(l=20, r=20, t=20, b=20),
    )
    
    graph_html = fig.to_html(full_html=False, default_height=500, default_width='100%')
    
    
    
    
        
    context = {
        'total_indicadores': total_indicadores,
        'ano_atual': ano_atual,
        'labels': labels,
        'data': data, 
        'graph_html': graph_html
    }
   
    
    return render(request, 'index.html', context=context)



def indicadores(request):
    
    indicadores = Indicador.objects.all()
    
    context = {
        'indicadores': indicadores,
    }
    
    return render(request, 'indicadores.html', context=context)


def indicador(request, gri_numero, indicador_id):
    gri = get_object_or_404(GRI, numero=gri_numero)
    indicador = get_object_or_404(Indicador, id=indicador_id, gri=gri)
    conteudo_atual = DadosConteudoIndicador.objects.filter(indicador=indicador, ano=date.today().year).first()
    conteudos_anteriores = DadosConteudoIndicador.objects.filter(indicador=indicador).exclude(ano=date.today().year)
    protocolo = ProtocoloGRI.objects.get(gri=indicador.gri)


    context = {
        'indicador': indicador,
        'protocolo': protocolo,
        'conteudo_atual': conteudo_atual,
        'conteudos_anteriores': conteudos_anteriores,
    }
    
    
    return render(request, 'indicador.html', context=context)

def gri(request, gri_slug):
    gri = get_object_or_404(GRI, slug=gri_slug) 
    gris = GRI.objects.get(slug=gri_slug)
    indicadores_relacionados = Indicador.objects.filter(gri=gri)
     
    context = {
        'gri': gri,
        'gris': gris,
        'indicadores_relacionados': indicadores_relacionados
    }   
    
    return render(request, 'GRI.html', context=context)

def informes(request):
    return render(request, 'informes.html')

def pmo(request):
    return render(request, 'pmo.html')
