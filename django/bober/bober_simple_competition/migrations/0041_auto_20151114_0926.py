# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0040_auto_20151112_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradedAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(null=True)),
                ('answer', models.ForeignKey(to='bober_simple_competition.Answer', on_delete=models.CASCADE)),
                ('attempt', models.ForeignKey(to='bober_simple_competition.Attempt', on_delete=models.CASCADE)),
                ('question', models.ForeignKey(to='bober_simple_competition.Question', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attempt',
            name='graded_answers',
            field=models.ManyToManyField(related_name='graded_attempt', null=True, through='bober_simple_competition.GradedAnswer', to='bober_simple_competition.Answer', blank=True),
            preserve_default=True,
        ),
    ]
