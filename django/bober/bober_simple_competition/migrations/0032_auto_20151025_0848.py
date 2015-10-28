# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0031_auto_20151025_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='shortened_code_bits',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='shortened_code_hash_algorithm',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='shortened_code_hash_format',
        ),
    ]
