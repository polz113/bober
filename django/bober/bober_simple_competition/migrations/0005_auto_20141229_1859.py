# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0004_auto_20141229_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='duration',
            field=models.IntegerField(default=3600),
        ),
    ]
