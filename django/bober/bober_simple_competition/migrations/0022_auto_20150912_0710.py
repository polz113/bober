# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0021_remove_profile_merged_with'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='merged_with_profile',
            new_name='merged_with',
        ),
    ]
