# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0005_auto_20141229_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='mimetype',
            field=models.CharField(default='img', max_length=255),
            preserve_default=False,
        ),
    ]
