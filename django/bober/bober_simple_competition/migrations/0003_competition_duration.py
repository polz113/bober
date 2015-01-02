# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0002_auto_20141227_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='duration',
            field=models.IntegerField(default=216000),
            preserve_default=True,
        ),
    ]
