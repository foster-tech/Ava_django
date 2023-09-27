from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Indicador, GRI

def index(request):
    
    gris = GRI.objects.all()
    
    context = {
        'gris': gris,
    }
   
    
    return render(request, 'index.html', context=context)



def indicadores(request):
    
    indicadores = Indicador.objects.all()
    
    context = {
        'indicadores': indicadores,
    }
    
    return render(request, 'indicadores.html', context=context)

def indicador(request, gri_nome, indicador_id):
    gri = get_object_or_404(GRI, nome=gri_nome)
    indicador = get_object_or_404(Indicador, id=indicador_id, gri=gri)
    
    context = {
        'indicador': indicador,
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
