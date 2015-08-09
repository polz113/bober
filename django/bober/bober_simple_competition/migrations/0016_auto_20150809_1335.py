# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0005_auto_20150117_1822'),
        ('bober_simple_competition', '0015_auto_20150809_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='update_managers_timestamp',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='update_used_codes_timestamp',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='used_codes',
            field=models.ManyToManyField(related_name='user_set', null=True, to='code_based_auth.Code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='received_codes',
            field=models.ManyToManyField(related_name='recipient_set', null=True, to='code_based_auth.Code', blank=True),
            preserve_default=True,
        ),
    ]
