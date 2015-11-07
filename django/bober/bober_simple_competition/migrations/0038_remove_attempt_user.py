# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0037_auto_20151106_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attempt',
            name='user',
        ),
    ]
