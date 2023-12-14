from django.db import models
from datetime import datetime, timedelta
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from usuarios.models import CustomUser, CustomUserManager
# models.py em meu_app
from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField(default='2023-01-01')
    data_fim = models.DateField(default='2023-01-01')
    
    def __str__(self):
        return self.nome
    
class Empresa(models.Model):
    nome = models.CharField(max_length = 140)
    
    def __str__(self) -> str:
        return self.nome

class Fabricante(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    nome = models.CharField(max_length= 140)
    
    def __str__(self) -> str:
        return self.nome

class Fabrica(models.Model):
    nome = models.CharField( max_length=50)
    fabricantes = models.ForeignKey(Fabricante, on_delete=models.CASCADE, default=1)
    
    def __str__(self) -> str:
        return self.nome

class GRI(models.Model):
    numero = models.CharField(max_length = 140)
    slug = models.SlugField(max_length=100, unique=True, default='', help_text='Numero do GRI ')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.numero)
        super(GRI, self).save(*args, **kwargs)    
    
    def __str__(self) -> str:
        return self.numero
    
class Status(models.Model):
    STATUS_CHOICES = [
        ('0', 'Em Andamento'),
        ('1', 'Não Iniciado'),
        ('2', 'A Validar'),
        ('3','Concluido' ),
        ('4', 'Em Atraso')
    ]
    
    valor = models.CharField(choices=STATUS_CHOICES, max_length=140)
    
    def __str__(self) -> str:
        return self.get_valor_display()
    
class Formulario(models.Model):
    nome_formulario = models.CharField(max_length=255, default=None)
    ano = models.IntegerField(default=datetime.now().year)
    comentario = models.CharField(max_length = 500, default=None)
    responsaveis = models.ManyToManyField('usuarios.CustomUser', related_name='responsaveis_indicadores', blank=True)
    validadores = models.ManyToManyField('usuarios.CustomUser', related_name='validadores_indicadores', blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='----')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.responsaveis.count() > 4:
            raise ValidationError("Você só pode adicionar até 4 responsáveis.")
        
        if self.validadores.count() > 4:
            raise ValidationError("Você só pode adicionar até 4 validadores.")
        
    def __str__(self) -> str:
        return self.nome_formulario   
    
    def get_status_display(self):
        return self.status.get_status_display()
    
    def get_absolute_url(self):
        return f'formulario/{self.id}/'
    
class InfoHead(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, default=None)
    info = models.TextField(default="") 
class TabelaConteudoIndicador(models.Model):
    
    OPTION_CHOICES = [
        ('0', 'Sim'),
        ('1', 'Nao')
    ]
    
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, default=None)
    possui_fabricante = models.CharField(choices=OPTION_CHOICES, max_length=1, default="")
    ano_criacao  = models.IntegerField(default=datetime.now().year)
    coluna_fixa = models.CharField(max_length=255, blank=True, null=True)
    
    colunas = models.JSONField(blank=True, null=True)
    dados = models.JSONField(blank=True, null=True)  

class DescricaoTabela(models.Model):
    tabela = models.ForeignKey(TabelaConteudoIndicador, on_delete=models.CASCADE)
    descricao = models.TextField(default="")     

class Perguntas(models.Model):
    tabela = models.ForeignKey(TabelaConteudoIndicador, on_delete=models.CASCADE, default=None)
    pergunta = models.TextField(default="") 
    resposta = models.TextField(default="" , blank=True, null=True)
    
class Indicador(models.Model):
    
    CATEGORIA_CHOICES = [
        ('Ambiental', 'Ambiental'),
        ('Social', 'Social'),
        ('Economico', 'Economico'),
        ('Setor', 'Setor')
    ]
    
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, default="")
    ano = models.IntegerField(default=datetime.now().year)
    tema = models.CharField(max_length = 140)
    gri = models.ForeignKey(GRI, on_delete=models.CASCADE)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=140)
    slug = models.SlugField(unique=False, default='', help_text='Nome do Tema')

    def save(self, *args, **kwargs):
        self.ano_criacao = datetime.now().year
        super(Indicador, self).save(*args, **kwargs)  
    
    def __str__(self) -> str:
        return self.gri.numero
      
class ProtocoloIndicador(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, default=None)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    descricao = models.TextField()
    tema_material = models.CharField(max_length = 200, default='')
    topico_gri = models.CharField(max_length = 200)
    relevancia = models.TextField()
    fontes = models.TextField()
    referencias = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return self.topico_gri

class DefinicoesProtocolo(models.Model):
    protocolo = models.ForeignKey(ProtocoloIndicador, on_delete=models.CASCADE)
    titulo = models.TextField(default="Definição de ")
    definicao = models.TextField()