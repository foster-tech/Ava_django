# Generated by Django 4.2.5 on 2023-10-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ava', '0009_alter_protocologri_fontes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocologri',
            name='fontes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='protocologri',
            name='references',
            field=models.TextField(blank=True),
        ),
    ]
