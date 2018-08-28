# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0035_auto_20151105_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('user', models.ForeignKey(blank=True, to='bober_simple_competition.Profile',
                                           null=True, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attempt',
            name='competitor',
            field=models.ForeignKey(blank=True, to='bober_simple_competition.Competitor',
                                    null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='promoted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
