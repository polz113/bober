# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0020_auto_20150912_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='merged_with',
        ),
    ]
