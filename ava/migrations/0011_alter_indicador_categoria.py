# Generated by Django 4.2.5 on 2023-10-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0010_alter_protocologri_fontes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='categoria',
            field=models.CharField(choices=[('Ambiental', 'Ambiental'), ('Social', 'Social'), ('Economico', 'Economico'), ('Setor', 'Setor')], max_length=140),
        ),
    ]
