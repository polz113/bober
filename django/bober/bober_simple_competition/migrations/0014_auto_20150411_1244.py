# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0013_auto_20150409_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_competition',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='registration_code',
        ),
    ]
