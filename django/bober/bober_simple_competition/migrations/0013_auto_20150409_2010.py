# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bober_simple_competition', '0012_auto_20150329_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttemptInvalidation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField(blank=True)),
                ('by', models.ForeignKey(to='bober_simple_competition.Profile',
                                         on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_competition',
            field=models.ForeignKey(blank=True, to='bober_simple_competition.Competition',
                                    null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='managed_users',
            field=models.ManyToManyField(related_name='managers', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attempt',
            name='invalidated_by',
            field=models.ForeignKey(blank=True, to='bober_simple_competition.AttemptInvalidation',
                                    null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
