# Generated by Django 4.2.5 on 2023-09-29 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0015_remove_indicador_medida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conteudoindicador',
            name='tema_material',
        ),
        migrations.AddField(
            model_name='conteudoindicador',
            name='tema_material',
            field=models.CharField(default='', max_length=200),
        ),
    ]
