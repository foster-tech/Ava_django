# Generated by Django 4.2.5 on 2023-10-19 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0035_perguntas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicador',
            name='pergunta',
        ),
    ]
