# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0023_auto_20150926_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='value',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
