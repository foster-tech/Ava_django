# Generated by Django 4.2.5 on 2023-10-19 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0033_alter_tarefa_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_inicio',
            field=models.DateField(default='1999-01-01'),
        ),
    ]