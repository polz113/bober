# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_si', '0002_auto_20151025_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='country_code',
            field=models.CharField(default='si', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.CharField(max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='headmaster',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='identifier',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='post',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='tax_number',
            field=models.CharField(max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
    ]
