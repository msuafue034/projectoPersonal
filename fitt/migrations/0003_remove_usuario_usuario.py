# Generated by Django 5.1.3 on 2025-02-12 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitt', '0002_rename_registro_registroactividad_objetivo_activado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='usuario',
        ),
    ]
