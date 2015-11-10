# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_tasks', '0002_remove_tasktranslation_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='country',
            field=models.CharField(default='SI', max_length=5),
            preserve_default=False,
        ),
    ]
