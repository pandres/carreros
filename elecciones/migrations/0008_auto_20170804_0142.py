# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0007_auto_20170804_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='orden',
            field=models.PositiveIntegerField(help_text='Orden opcion', null=True),
        ),
        migrations.AlterField(
            model_name='opcion',
            name='orden',
            field=models.PositiveIntegerField(help_text='Orden opcion para votos no positivos', null=True),
        ),
    ]
