from django.urls import path
from .views import index, indicadores ,indicador, informes, pmo, gri

urlpatterns =[  
    path('', index, name="index"),
    path('indicadores/', indicadores, name="indicadores"), 
    path('indicadores/<str:gri_nome>/<int:indicador_id>/', indicador, name="indicador"),
    path('gri/<str:gri_slug>', gri, name="gri"),
    path('informes/', informes, name="informes"),
    path('pmo/', pmo, name="pmo"),
]