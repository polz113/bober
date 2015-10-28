# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0006_auto_20151016_1957'),
        ('bober_simple_competition', '0025_auto_20150927_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short', models.CharField(max_length=256)),
                ('code', models.ForeignKey(to='code_based_auth.Code')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='competitionquestionset',
            name='shortened_codes',
            field=models.ManyToManyField(to='bober_simple_competition.ShortenedCode', null=True, blank=True),
            preserve_default=True,
        ),
    ]
