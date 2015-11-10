# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_tasks', '0004_auto_20151109_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasktranslation',
            old_name='translator',
            new_name='author',
        ),
    ]
