# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0038_remove_attempt_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='first_name',
            field=models.CharField(max_length=128, verbose_name='First Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competitor',
            name='last_name',
            field=models.CharField(max_length=128, verbose_name='Last Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.CharField(max_length=7, choices=[(b'sl', 'Slovenian')]),
            preserve_default=True,
        ),
    ]
