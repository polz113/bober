# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_tasks', '0003_task_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktranslation',
            name='template',
            field=models.CharField(default='default', max_length=255, choices=[(b'default', b'default.html')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='interaction_type',
            field=models.CharField(default=b'non-interactive', max_length=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='international_id',
            field=models.CharField(unique=True, max_length=16),
            preserve_default=True,
        ),
    ]
