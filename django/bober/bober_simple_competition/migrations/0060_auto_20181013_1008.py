# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-10-13 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0059_auto_20181002_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female'), ('na', 'Not applicable')], max_length=16),
        ),
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.CharField(choices=[('sl', 'Slovenian'), ('sr_', 'Serbian'), ('en', 'English'), ('tr', 'Turkish')], max_length=7),
        ),
    ]
