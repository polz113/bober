# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-12 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_si', '0007_teachercompetitionrecognition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='competition',
        ),
        migrations.AlterField(
            model_name='award',
            name='template',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
