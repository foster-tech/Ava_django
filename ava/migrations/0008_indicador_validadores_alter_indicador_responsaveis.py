# Generated by Django 4.2.5 on 2023-10-11 03:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ava', '0007_remove_indicador_responsavel_indicador_responsaveis'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='validadores',
            field=models.ManyToManyField(related_name='validadores_indicadores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='indicador',
            name='responsaveis',
            field=models.ManyToManyField(related_name='responsaveis_indicadores', to=settings.AUTH_USER_MODEL),
        ),
    ]
