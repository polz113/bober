# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0005_auto_20150117_1822'),
        ('bober_simple_competition', '0014_auto_20150411_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='guest_code',
        ),
        migrations.AddField(
            model_name='competitionquestionset',
            name='guest_code',
            field=models.ForeignKey(blank=True, to='code_based_auth.Code',
                                    null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='managed_users',
            field=models.ManyToManyField(related_name='managers', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
