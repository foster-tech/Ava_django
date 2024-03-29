# Generated by Django 4.2.5 on 2023-10-16 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0021_dadosconteudoindicador_resp_indicador'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='quant_colunas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='InformacoesTabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_1', models.CharField(blank=True, max_length=100, null=True)),
                ('campo_2', models.CharField(blank=True, max_length=100, null=True)),
                ('indicador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='informacoes_tabela_rel', to='ava.indicador')),
            ],
        ),
        migrations.AddField(
            model_name='indicador',
            name='informacoes_tabela',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indicador_rel', to='ava.informacoestabela'),
        ),
    ]
