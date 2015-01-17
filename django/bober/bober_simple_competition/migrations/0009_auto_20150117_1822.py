# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0008_profile_received_codes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='user',
            field=models.ForeignKey(blank=True, to='bober_simple_competition.Profile', null=True),
            preserve_default=True,
        ),
    ]
