# No arquivo forms.py
from django import forms
from .models import Indicador

class IndicadorAdminForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = ['tema', 'gri', 'comentario', 'status', 'categoria',  'responsaveis', 'validadores', 'slug',]
