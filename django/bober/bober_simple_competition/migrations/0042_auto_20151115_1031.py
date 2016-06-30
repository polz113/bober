# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0041_auto_20151114_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attempt',
            name='graded_answers',
        ),
        migrations.AlterField(
            model_name='answer',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
