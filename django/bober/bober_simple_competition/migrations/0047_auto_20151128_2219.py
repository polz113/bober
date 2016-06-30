# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0046_auto_20151125_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionset',
            name='questions',
            field=models.ManyToManyField(to='bober_simple_competition.Question', blank=True),
        ),
    ]
