# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-08-28 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_si', '0016_auto_20180320_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardfile',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]