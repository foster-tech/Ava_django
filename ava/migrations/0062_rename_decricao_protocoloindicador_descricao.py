# Generated by Django 4.2.7 on 2023-11-26 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0061_remove_formulario_tabela_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='protocoloindicador',
            old_name='decricao',
            new_name='descricao',
        ),
    ]
