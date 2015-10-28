# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0027_auto_20151017_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='feature_level',
            field=models.IntegerField(default=1, choices=[(0, 'Reduced functionality'), (1, 'Basic features only'), (10, 'Commonly used features'), (128, 'All features')]),
            preserve_default=True,
        ),
    ]
