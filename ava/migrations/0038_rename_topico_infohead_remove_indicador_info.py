# Generated by Django 4.2.5 on 2023-10-23 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0037_rename_pergunta_topico_info'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topico',
            new_name='InfoHead',
        ),
        migrations.RemoveField(
            model_name='indicador',
            name='info',
        ),
    ]
