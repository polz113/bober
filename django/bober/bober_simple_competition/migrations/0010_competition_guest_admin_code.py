# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0005_auto_20150117_1822'),
        ('bober_simple_competition', '0009_auto_20150117_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='guest_admin_code',
            field=models.ForeignKey(to='code_based_auth.Code', null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
