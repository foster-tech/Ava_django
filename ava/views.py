from django.shortcuts import render, get_object_or_404
import calendar
from datetime import date, datetime, timedelta
from django.db.models import Count
from .models import Indicador, GRI, ProtocoloGRI, DadosConteudoIndicador, Status, Tarefa

def index(request):
    ano_atual = datetime.now().year
    total_indicadores = Indicador.objects.count()
    
    status_counts = Status.objects.annotate(indicador_count=Count('indicador'))
    status_counts_dict = {status.get_valor_display(): status.indicador_count for status in status_counts}
    
    labels = [status[1] for status in Status.STATUS_CHOICES]
    data = [status_counts_dict.get(status[1], 0) for status in Status.STATUS_CHOICES]
        
    context = {
        'total_indicadores': total_indicadores,
        'ano_atual': ano_atual,
        'labels': labels,
        'data': data, 
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
