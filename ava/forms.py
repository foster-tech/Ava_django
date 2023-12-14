# No arquivo forms.py
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Formulario
    
class FormularioAdminForm(forms.ModelForm):
     class Meta:
        model = Formulario
        fields = ['nome_formulario','ano','status','comentario','responsaveis', 'validadores']
        
        
