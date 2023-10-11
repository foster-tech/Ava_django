from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.core.exceptions import ValidationError
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
        ('Economico', 'Economico'),
        ('Setor', 'Setor')
    ]
    
    tema = models.CharField(max_length = 140)
    gri = models.ForeignKey(GRI, on_delete=models.CASCADE)
    responsaveis = models.ManyToManyField('usuarios.CustomUser', related_name='responsaveis_indicadores', blank=True)
    validadores = models.ManyToManyField('usuarios.CustomUser', related_name='validadores_indicadores', blank=True)
    comentario = models.CharField(max_length = 500)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=140)
    ano_criacao  = models.IntegerField(default=datetime.now().year)
    slug = models.SlugField(unique=False, default='', help_text='Nome do Tema')

    def save(self, *args, **kwargs):
        
        self.ano_criacao = datetime.now().year
        super(Indicador, self).save(*args, **kwargs)
        
        if self.responsaveis.count() > 4:
            raise ValidationError("Você só pode adicionar até 4 responsáveis.")
        
        if self.validadores.count() > 4:
            raise ValidationError("Você só pode adicionar até 4 validadores.")
        
        
        
    
    def __str__(self) -> str:
        return self.gri.numero
    
    def get_absolute_url(self):
        return f'indicadores/{self.gri}/{self.id}/'
    
    def alterar_status(self, novo_status, usuario):
        antigo_status = self.status
        self.status = novo_status
        self.save()
    
        
    def get_status_display(self):
        return self.status.get_status_display()

class DadosConteudoIndicador(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, default='')
    ano = models.PositiveIntegerField(default=1999)
    
       

class GrupoInformacoes(models.Model):
    CERTIFICADA = [
        (1, 'Sim'),
        (2, 'Não'),
    ]
    
    dados_conteudo = models.ForeignKey(DadosConteudoIndicador, on_delete=models.CASCADE)
    fabricante = models.CharField(max_length=150)
    fabrica = models.CharField(max_length=150)
    e_certificada = models.IntegerField(choices=CERTIFICADA)
    justificativa = models.TextField(blank=True, null=True)

    def definir_justificativa(self):
        if self.e_certificada == 2:
            self.justificativa = "Justificativa aqui"
        else:
            self.justificativa = ""

    


class HistoricoIndicador(models.Model):
    ano = models.IntegerField(default=1999)
    
    def __str__(self):
        return f'{self.indicador} - {self.novo_status}'
    
class ProtocoloGRI(models.Model):
    gri = models.ForeignKey(GRI, on_delete=models.CASCADE)
    decricao = models.TextField()
    tema_material = models.CharField(max_length = 200, default='')
    topico_gri = models.CharField(max_length = 200)
    relevancia = models.TextField()
    fontes = models.TextField()
    references = models.TextField(blank=True)
    definicoes = models.TextField()
    
    def __str__(self) -> str:
        return self.tema_material
    
class HistoricoGRI(models.Model):
    gri = models.ForeignKey(GRI, on_delete=models.CASCADE)
    novo_numero = models.CharField(max_length=100)
    ano_mudanca = models.IntegerField()
    
    def __str__(self):
        return f'{self.gri} - {self.novo_numero} ({self.ano_mudanca})'




