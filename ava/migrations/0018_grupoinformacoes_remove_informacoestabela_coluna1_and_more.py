# Generated by Django 4.2.5 on 2023-10-16 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0017_empresa_fabrica_fabricante_informacoestabela_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoInformacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=150)),
                ('fabrica', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='informacoestabela',
            name='coluna1',
        ),
        migrations.RemoveField(
            model_name='informacoestabela',
            name='coluna2',
        ),
        migrations.RemoveField(
            model_name='informacoestabela',
            name='dados_conteudo',
        ),
        migrations.DeleteModel(
            name='UnidadesMedidas',
        ),
        migrations.RemoveField(
            model_name='dadosconteudoindicador',
            name='quantidade_colunas',
        ),
        migrations.AddField(
            model_name='indicador',
            name='pergunta',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='InformacoesTabela',
        ),
        migrations.AddField(
            model_name='grupoinformacoes',
            name='dados_conteudo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ava.dadosconteudoindicador'),
        ),
    ]
