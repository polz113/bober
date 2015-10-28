# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def len_from_bits(apps, schema_editor):
    CodeComponent = apps.get_model("code_based_auth", "CodeComponent")
    import math
    for cc in CodeComponent.objects.all():
        cc.hash_len = math.ceil(cc.hash_bits / 8.0)
        cc.save()

def bits_from_len(apps, schema_editor):
    CodeComponent = apps.get_model("code_based_auth", "CodeComponent")
    import math
    for cc in CodeComponent.objects.all():
        cc.hash_bits = math.ceil(cc.hash_len * 8)
        cc.save()

class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0007_auto_20151021_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='codecomponent',
            name='hash_len',
            field=models.PositiveIntegerField(default=42),
            preserve_default=False,
        ),
        migrations.RunPython(len_from_bits, bits_from_len),
        migrations.RemoveField(
            model_name='codecomponent',
            name='hash_bits',
        ),
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_format',
            field=models.CharField(max_length=2, choices=[(b'h', b'hex'), (b'i', b'decimal'), (b'l', b'letters and digits'), (b'L', b'case-insensitive letters and digits'), (b'w', b'words'), (b'W', b'case-insensitive words'), (b'r', b'raw no hash')]),
            preserve_default=True,
        ),
    ]
