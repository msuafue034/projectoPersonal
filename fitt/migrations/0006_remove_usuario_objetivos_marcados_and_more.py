# Generated by Django 5.1.3 on 2025-02-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitt', '0005_auto_20250220_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='objetivos_marcados',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='objetivos',
            field=models.ManyToManyField(blank=True, through='fitt.ObjetivoUsuario', to='fitt.objetivo'),
        ),
    ]
