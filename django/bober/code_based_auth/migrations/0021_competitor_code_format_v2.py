from django.db import migrations

V2_FORMAT_NAME = "Competitor code v2"


def create_v2_competitor_format(apps, schema_editor):
    """Add a v2 competitor code format so new competitions can select it.

    Only inserts rows; existing formats, generators and codes are untouched.
    Mirrors CodeFormat.create_v2() (historical models have no custom methods).
    """
    CodeFormat = apps.get_model("code_based_auth", "CodeFormat")
    CodeComponent = apps.get_model("code_based_auth", "CodeComponent")
    if CodeFormat.objects.filter(code_version=2).exists():
        return
    cf = CodeFormat.objects.create(
        name=V2_FORMAT_NAME, separator="*", code_version=2)
    components = [
        {"name": "competition_questionset", "hash_format": "r",
         "hash_algorithm": "noop", "hash_len": 256, "max_parts": 1},
        {"name": "code_id", "hash_format": "S",
         "hash_algorithm": "noop", "hash_len": 6, "max_parts": 1},
        {"name": "competitor_privileges", "hash_format": "S",
         "hash_algorithm": "noop", "hash_len": 1, "max_parts": 4},
    ]
    for i, c in enumerate(components):
        CodeComponent.objects.create(code_format=cf, ordering=i, **c)


class Migration(migrations.Migration):

    dependencies = [
        ("code_based_auth", "0020_codeformat_code_version"),
    ]

    operations = [
        migrations.RunPython(create_v2_competitor_format,
                             migrations.RunPython.noop),
    ]
