# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0036_auto_20151106_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competitor',
            old_name='user',
            new_name='profile',
        ),
    ]
