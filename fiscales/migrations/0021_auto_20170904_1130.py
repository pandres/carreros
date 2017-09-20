# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fiscales', '0020_asignacionfiscalgeneral_eleccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiscal',
            name='codigo_confirmacion',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='fiscal',
            name='email_confirmado',
            field=models.BooleanField(default=False),
        ),
    ]