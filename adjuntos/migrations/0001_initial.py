# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elecciones', '0022_auto_20171014_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mimetype', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='attachments/')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('from_address', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('title', models.CharField(max_length=50)),
                ('uid', models.PositiveIntegerField()),
                ('message_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='attachment',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adjuntos.Email'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='mesa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elecciones.Mesa'),
        ),
    ]
