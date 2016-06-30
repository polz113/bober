# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0042_auto_20151115_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='score',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
