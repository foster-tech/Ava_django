# Generated by Django 4.2.7 on 2023-11-24 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0051_remove_indicador_responsaveis_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicador',
            name='status',
        ),
        migrations.AddField(
            model_name='formulario',
            name='status',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='ava.status'),
        ),
    ]