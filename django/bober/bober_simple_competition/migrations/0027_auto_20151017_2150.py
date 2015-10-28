# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0026_auto_20151016_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitionquestionset',
            name='shortened_codes',
        ),
        migrations.AddField(
            model_name='competition',
            name='shortened_code_bits',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='shortened_code_hash_algorithm',
            field=models.CharField(blank=True, max_length=16, null=True, choices=[(b'md5', b'md5'), (b'sha1', b'sha1'), (b'sha224', b'sha224'), (b'sha256', b'sha256'), (b'sha384', b'sha384'), (b'sha512', b'sha512'), (b'noop', b'No hash')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='shortened_code_hash_format',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'h', b'hex'), (b'i', b'decimal'), (b'w', b'words'), (b'r', b'raw no hash'), (b'a', b'match exact')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shortenedcode',
            name='competition_question_set',
            field=models.ForeignKey(default=1, to='bober_simple_competition.CompetitionQuestionSet'),
            preserve_default=False,
        ),
    ]
