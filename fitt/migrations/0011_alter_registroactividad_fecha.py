# Generated by Django 5.1.3 on 2025-02-21 00:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitt', '0010_auto_20250221_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroactividad',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha'),
        ),
    ]
