# Generated by Django 4.2.5 on 2023-10-13 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0016_alter_grupoinformacoes_e_certificada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Fabrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='InformacoesTabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coluna1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ava.fabricante')),
                ('coluna2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ava.fabrica')),
            ],
        ),
        migrations.AddField(
            model_name='dadosconteudoindicador',
            name='quantidade_colunas',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='GrupoInformacoes',
        ),
        migrations.AddField(
            model_name='informacoestabela',
            name='dados_conteudo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ava.dadosconteudoindicador'),
        ),
        migrations.AddField(
            model_name='fabrica',
            name='fabricante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ava.fabricante'),
        ),
    ]
