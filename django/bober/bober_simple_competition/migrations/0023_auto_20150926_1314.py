# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0022_auto_20150912_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='questions',
            field=models.ManyToManyField(to='bober_simple_competition.Question', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='merged_with',
            field=models.ForeignKey(related_name='former_profile_set', blank=True,
                                    to='bober_simple_competition.Profile',
                                    null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='verification_function_type',
            field=models.IntegerField(default=0, choices=[(0, b'none'), (1, b'javascript'), (2, b'python')]),
            preserve_default=True,
        ),
    ]
