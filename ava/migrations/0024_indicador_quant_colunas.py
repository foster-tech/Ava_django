# Generated by Django 4.2.5 on 2023-10-16 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0023_remove_indicador_informacoes_tabela_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='quant_colunas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
