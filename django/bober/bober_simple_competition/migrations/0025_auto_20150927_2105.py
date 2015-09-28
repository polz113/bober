# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
def move_accepted_answers(apps, schema_editor):
    Question = apps.get_model("bober_simple_competition", "Question")
    for q in Question.objects.all():
        q.verification_function = q.accepted_answers
        q.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0024_auto_20150926_1340'),
    ]

    operations = [
        migrations.RunPython(move_accepted_answers),
        migrations.RemoveField(
            model_name='question',
            name='accepted_answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='max_score',
            field=models.FloatField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='min_score',
            field=models.FloatField(default=-1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='none_score',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='verification_function_type',
            field=models.IntegerField(default=0, choices=[(0, b'none'), (1, b'javascript_gostisa'), (2, b'javascript_france'), (16, b'python')]),
            preserve_default=True,
        ),
    ]
