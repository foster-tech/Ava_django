# Generated by Django 4.2.7 on 2023-12-11 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0064_alter_status_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabelaconteudoindicador',
            name='resposta',
        ),
    ]
