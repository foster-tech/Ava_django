from django.contrib import admin
from .forms import FormularioAdminForm
from .models import Indicador, Status, ProtocoloIndicador, Fabrica, Perguntas, InfoHead, Formulario, TabelaConteudoIndicador, DescricaoTabela, DefinicoesProtocolo
import django.apps

@admin.register(Fabrica)
class FabricaAdmin(admin.ModelAdmin):
    ordering = ['nome']


class PerguntasInline(admin.TabularInline):
    model = Perguntas
    
class InfoHeadInline(admin.TabularInline):
    model = InfoHead

class DescricaoTabelaInline(admin.TabularInline):
    model = DescricaoTabela
    
class DefinicoesProtocoloInline(admin.TabularInline):
    model = DefinicoesProtocolo

@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
     inlines =  [InfoHeadInline]
     list_display = ('nome_formulario','status','ano')
     form = FormularioAdminForm
     filter_horizontal = ('responsaveis', 'validadores') 

@admin.register(TabelaConteudoIndicador)
class TabelaConteudoIndicadorFormularioAdmin(admin.ModelAdmin):
    inlines = [DescricaoTabelaInline, PerguntasInline]
    list_display = ('formulario','ano_criacao')
        
@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ('gri','tema','categoria', 'ano')
    list_filter = ('categoria',)
    search_fields = ('categoria',)

    def inficador_link(self, obj):
        return f'<a href="{obj.get_absolute_url()}">{obj.nome}</a>'
    
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display=['valor']
    
@admin.register(ProtocoloIndicador)
class ProtocoloIndicadorAdmin(admin.ModelAdmin):
    inlines =  [DefinicoesProtocoloInline]
    list_display=['topico_gri', 'indicador',]


models = django.apps.apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass



    

