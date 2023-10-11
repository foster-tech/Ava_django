# Generated by Django 4.2.5 on 2023-10-11 04:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ava', '0011_alter_indicador_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='responsaveis',
            field=models.ManyToManyField(blank=True, related_name='responsaveis_indicadores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='indicador',
            name='validadores',
            field=models.ManyToManyField(blank=True, related_name='validadores_indicadores', to=settings.AUTH_USER_MODEL),
        ),
    ]
