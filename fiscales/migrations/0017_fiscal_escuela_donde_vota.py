# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0020_auto_20170901_0026'),
        ('fiscales', '0016_auto_20170901_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiscal',
            name='escuela_donde_vota',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elecciones.LugarVotacion'),
        ),
    ]
