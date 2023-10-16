from django.contrib import admin
from .forms import IndicadorAdminForm, GrupoInformacoesForm
from .models import Indicador,HistoricoIndicador, GRI, Status, ProtocoloGRI, DadosConteudoIndicador, GrupoInformacoes, Fabrica, Fabricante
import django.apps

@admin.register(Fabrica)
class FabricaAdmin(admin.ModelAdmin):
    ordering = ['nome']

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    form = IndicadorAdminForm
    list_display = ('tema', 'gri', 'comentario', 'categoria', 'ano_criacao', 'resposta', 'pergunta')
    list_filter = ('tema', 'categoria')
    list_editable = ('resposta',)
    search_fields = ('tema', 'categoria')
    filter_horizontal = ('responsaveis', 'validadores') 

    def inficador_link(self, obj):
        return f'<a href="{obj.get_absolute_url()}">{obj.nome}</a>'
    
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        obj.save()
    
    def save_model(self, request, obj, form, change):
        # Registra a alteração no histórico
            if change:
                novo_status = form.cleaned_data['status']
                if novo_status != obj.status:
                    HistoricoIndicador.objects.create(
                        produto=obj,
                        novo_status=novo_status,
                        responsavel=request.user
                    )
            super().save_model(request, obj, form, change)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display=['valor']
    
@admin.register(ProtocoloGRI)
class ProtocoloGRIAdmin(admin.ModelAdmin):
    list_display=['tema_material', 'topico_gri']

class GrupoInformacoesInline(admin.TabularInline):
    model = GrupoInformacoes
    form = GrupoInformacoesForm
    
@admin.register(DadosConteudoIndicador)
class DadosConteudoIndicadorAdmin(admin.ModelAdmin):
    inlines = [GrupoInformacoesInline]
    list_display=('indicador', 'ano')
    


        


models = django.apps.apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass



    

