# Generated by Django 4.2.5 on 2023-10-11 02:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ava', '0002_remove_indicador_responsavel_indicador_responsavel'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='validador',
            field=models.ManyToManyField(limit_choices_to={'responsavel__count__lte': 4}, related_name='validador_indicadores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='indicador',
            name='responsavel',
            field=models.ManyToManyField(limit_choices_to={'responsavel__count__lte': 4}, to=settings.AUTH_USER_MODEL),
        ),
    ]
