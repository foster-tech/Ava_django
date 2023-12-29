from django.urls import path
from .views import index, formularios ,indicador, informes, pmo, atualizar_totais, consolidado, status, comunicados

urlpatterns =[  
    path('', index, name="index"),
    path('atualizar_totais/', atualizar_totais, name='atualizar_totais'),
    path('formularios/', formularios, name="formularios"), 
    path('formularios/<int:formulario_id>/', indicador, name="indicador"),
    path('consolidado/', consolidado, name="consolidado"),
    path('status/', status, name="status"),
    path('comunicados/', comunicados, name="comunicados"),
    path('informes/', informes, name="informes"),
    path('pmo/', pmo, name="pmo"),
]