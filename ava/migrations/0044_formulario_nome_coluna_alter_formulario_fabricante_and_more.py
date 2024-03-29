# Generated by Django 4.2.7 on 2023-11-23 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0043_remove_grupoinformacoes_fabrica_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='nome_coluna',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='fabricante',
            field=models.ForeignKey(default='---', on_delete=django.db.models.deletion.CASCADE, to='ava.fabricante'),
        ),
        migrations.CreateModel(
            name='DescricaoColunaForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(default='')),
                ('formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ava.formulario')),
            ],
        ),
    ]
