# Generated by Django 4.2.5 on 2023-10-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0039_remove_tarefa_duracao_semanas_tarefa_data_fim_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_fim',
            field=models.DateField(default='2023-01-01'),
        ),
    ]