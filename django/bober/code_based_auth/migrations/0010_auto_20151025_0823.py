# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0009_auto_20151025_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codepart',
            name='value',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
    ]
