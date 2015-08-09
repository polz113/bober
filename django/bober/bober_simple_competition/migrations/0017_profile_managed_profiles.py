# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def managed_users_to_profiles(apps, schema_editor):
    Profile = apps.get_model("bober_simple_competition", "Profile")
    for p in Profile.objects.all():
        for u in p.managed_users.all():
            try:
                p.managed_profiles.add(u.profile)
            except Exception, e:
                print e
        

class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0016_auto_20150809_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='managed_profiles',
            field=models.ManyToManyField(related_name='managers', null=True, to='bober_simple_competition.Profile', blank=True),
            preserve_default=True,
        ),
        migrations.RunPython(managed_users_to_profiles)
    ]
