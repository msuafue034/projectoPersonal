# Generated by Django 5.1.4 on 2025-01-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitt', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registro',
            new_name='RegistroActividad',
        ),
        migrations.AddField(
            model_name='objetivo',
            name='activado',
            field=models.BooleanField(default=False, verbose_name='Activado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='objetivos_marcados',
            field=models.BooleanField(default=False, verbose_name='Objetivos marcados'),
        ),
    ]
