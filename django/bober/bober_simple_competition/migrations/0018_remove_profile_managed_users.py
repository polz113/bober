# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0017_profile_managed_profiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='managed_users',
        ),
    ]
