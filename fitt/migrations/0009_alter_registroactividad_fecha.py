# Generated by Django 5.1.3 on 2025-02-20 23:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitt', '0008_remove_objetivousuario_tiempo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroactividad',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now, unique=True, verbose_name='Fecha'),
        ),
    ]
