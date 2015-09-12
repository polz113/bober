# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def merged_user_to_profile(apps, schema_editor):
    Profile = apps.get_model('bober_simple_competition', 'Profile')
    for p in Profile.objects.all():
        if p.merged_with is not None:
            p.merged_with_profile = p.merged_with.profile

class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0019_auto_20150908_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='merged_with_profile',
            field=models.ForeignKey(related_name='merged_profile_set', blank=True, to='bober_simple_competition.Profile', null=True),
            preserve_default=True,
        ),
        migrations.RunPython(merged_user_to_profile),
        migrations.AlterField(
            model_name='profile',
            name='created_codes',
            field=models.ManyToManyField(related_name='creator_set', null=True, to='code_based_auth.Code', blank=True),
            preserve_default=True,
        ),
    ]
