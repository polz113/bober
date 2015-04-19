# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0005_auto_20150117_1822'),
        ('bober_simple_competition', '0010_competition_guest_admin_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='guest_admin_code',
            new_name='guest_code',
        ),
    ]
