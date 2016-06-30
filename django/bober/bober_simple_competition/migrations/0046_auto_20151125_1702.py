# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0045_auto_20151125_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='confirmed_by',
            field=models.ManyToManyField(to='bober_simple_competition.Profile', through='bober_simple_competition.AttemptConfirmation', blank=True),
        ),
    ]
