from django.urls import path
from .views import index, indicadores ,indicador, informes, pmo

urlpatterns =[  
    path('', index, name="index"),
    path('indicadores/', indicadores, name="indicadores"), 
    path('indicadores/<str:gri_numero>/<int:indicador_id>/', indicador, name="indicador"),
    path('informes/', informes, name="informes"),
    path('pmo/', pmo, name="pmo"),
]