# Generated by Django 4.2.7 on 2023-11-24 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0056_definicioesprotocolo_protocoloindicador_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infohead',
            name='indicador',
        ),
        migrations.AddField(
            model_name='infohead',
            name='formulario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ava.formulario'),
        ),
    ]
