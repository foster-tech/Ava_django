# No arquivo forms.py
from django import forms
from .models import Indicador, GrupoInformacoes

class IndicadorAdminForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = ['tema', 'gri', 'comentario', 'status', 'categoria','colunas','dados','responsaveis', 'validadores', 'slug',]

class GrupoInformacoesForm(forms.ModelForm):
    class Meta:
        model = GrupoInformacoes
        fields = ['dados_conteudo', 'fabricante', 'fabrica']  # Adicione os campos aqui
        
