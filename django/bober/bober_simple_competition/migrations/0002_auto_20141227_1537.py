# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='part_of_solution',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='vcard',
            field=models.TextField(blank=True),
        ),
    ]
