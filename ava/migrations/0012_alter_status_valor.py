# Generated by Django 4.2.5 on 2023-09-27 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0011_alter_unidadesmedidas_medidas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='valor',
            field=models.CharField(choices=[('0', 'Iniciado'), ('1', 'Não Iniciado'), ('2', 'A Validar'), ('3', 'Concluido')], max_length=140),
        ),
    ]
