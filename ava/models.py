from django.db import models
from datetime import date
from django.utils.text import slugify
from usuarios.models import CustomUser, CustomUserManager

class GRI(models.Model):
    porcentagem = models.FloatField(null=True, blank=True, default=None)
    numero = models.CharField(max_length = 140)
    ano_mudanca = models.IntegerField(blank=True, null=True, default='GRI-')
    slug = models.SlugField(max_length=100, unique=True, default='', help_text='Numero do GRI ')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.numero)
        super(GRI, self).save(*args, **kwargs)    
    
    def __str__(self) -> str:
        return self.numero
    
    def alterar_numero_gri(gri, novo_numero, ano_mudanca):
        gri.numero = novo_numero
        gri.ano_mudanca = ano_mudanca
        gri.save()

        HistoricoGRI.objects.create(
            gri=gri,
            novo_numero=novo_numero,
            ano_mudanca=ano_mudanca
        )
    


class Status(models.Model):
    STATUS_CHOICES = [
        ('0', 'Iniciado'),
        ('1', 'Não Iniciado'),
        ('2', 'A Validar'),
        ('3','Concluido' )
    ]
    
    valor = models.CharField(choices=STATUS_CHOICES, max_length=140)
    
    def __str__(self) -> str:
        return self.get_valor_display()
    

class UnidadesMedidas(models.Model):
    VOLUMES_CHOICES = [
        ('l', 'Litros'),
        ('kg', 'Quilogramas'),
        ('m3', 'Metro Cúbico'),
        ('m', 'Metros' ),
        ('g', 'Gramas'),
    ]
    
    MEDIDAS_CHOICES = [
        ('capacidade', 'Capacidade'),
        ('comprimento', 'Comprimento'),
        ('massa','Massa' ),
        ('volume', 'Volume' ),
    ]
    
    medidas = models.CharField(choices=MEDIDAS_CHOICES, max_length=140)  
    volumes = models.CharField(choices=VOLUMES_CHOICES, max_length=140)
    
    def __str__(self) -> str:
        return self.get_volumes_display()
    
    
class Indicador(models.Model):
    
    CATEGORIA_CHOICES = [
        ('Ambiental', 'Ambiental'),
        ('Social', 'Social'),
        ('Economico', 'Economico')
    ]
    
    tema = models.CharField(max_length = 140)
    gri = models.ForeignKey(GRI, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comentario = models.CharField(max_length = 500)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=140)
    data = models.DateField(("Date"), default=date.today)
    slug = models.SlugField(unique=False, default='', help_text='Nome do Tema')

    
    def __str__(self) -> str:
        return self.gri.numero
    
    def get_absolute_url(self):
        return f'indicadores/{self.gri}/{self.id}/'
    
    
    def alterar_status(self, novo_status, usuario):
        antigo_status = self.status
        self.status = novo_status
        self.save()

        HistoricoIndicador.objects.create(
            produto=self,
            antigo_status=antigo_status,
            novo_status=novo_status,
            usuario=usuario
        )    
        
    def get_status_display(self):
        return self.status.get_status_display()




class ConteudoIndicador(models.Model):
    decricao = models.TextField()
    tema_material = models.CharField(max_length = 200, default='')
    topico_gri = models.CharField(max_length = 200)
    relevancia = models.TextField()
    fontes = models.TextField()
    references = models.TextField(default='')
    definicoes = models.TextField()
    
    def __str__(self) -> str:
        return self.tema_material
    
    

class HistoricoIndicador(models.Model):
    indicador = models.ForeignKey('Indicador', on_delete=models.CASCADE)
    antigo_status = models.CharField(max_length=100, default='')
    novo_status = models.CharField(max_length=50, default='')
    data_alteracao = models.DateTimeField(auto_now_add=True)
    responsavel = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.indicador} - {self.novo_status}'
    
class HistoricoGRI(models.Model):
    gri = models.ForeignKey(GRI, on_delete=models.CASCADE)
    novo_numero = models.CharField(max_length=100)
    ano_mudanca = models.IntegerField()
    
    def __str__(self):
        return f'{self.gri} - {self.novo_numero} ({self.ano_mudanca})'




