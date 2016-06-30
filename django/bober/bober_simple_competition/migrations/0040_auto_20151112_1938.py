# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0039_auto_20151108_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttemptConfirmation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attempt', models.ForeignKey(to='bober_simple_competition.Attempt')),
                ('by', models.ForeignKey(to='bober_simple_competition.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attempt',
            name='confirmed_by',
            field=models.ManyToManyField(to='bober_simple_competition.Profile', null=True, through='bober_simple_competition.AttemptConfirmation', blank=True),
            preserve_default=True,
        ),
    ]
