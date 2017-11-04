# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0055_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='duration',
            field=models.IntegerField(default=2700, help_text='Duration of the competition in seconds', verbose_name='duration'),
        ),
    ]
