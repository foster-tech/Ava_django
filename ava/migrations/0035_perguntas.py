# Generated by Django 4.2.5 on 2023-10-19 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0034_alter_tarefa_data_inicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.TextField(default='')),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ava.indicador')),
            ],
        ),
    ]
