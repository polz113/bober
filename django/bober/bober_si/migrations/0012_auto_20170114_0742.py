# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-14 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_si', '0011_award_replaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='replaces',
            field=models.ManyToManyField(related_name='replaced_by', to='bober_si.Award'),
        ),
    ]
