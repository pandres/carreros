# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prensa', '0004_auto_20170801_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datodecontacto',
            name='tipo',
            field=models.CharField(choices=[('teléfono', 'teléfono'), ('email', 'email'), ('web', 'web'), ('twitter', 'twitter'), ('facebook', 'facebook'), ('instagram', 'instagram'), ('youtube', 'youtube'), ('skype', 'skype')], max_length=20),
        ),
    ]