
from django.db import migrations, models

V2_ADMIN_FORMAT_NAME = "Admin code v2"
ADMIN_FLAG_COMPONENTS = (
    ("admin_privileges", 8),
    ("allowed_effects", 2),
    ("competitor_privileges", 4),
)


def create_v2_admin_format(apps, schema_editor):
    """Add a v2 administrator code format (inserts rows only).

    Mirrors CodeFormat.create_admin_v2() (historical models have no custom
    methods).
    """
    CodeFormat = apps.get_model("code_based_auth", "CodeFormat")
    CodeComponent = apps.get_model("code_based_auth", "CodeComponent")
    if CodeFormat.objects.filter(code_version=3).exists():
        return
    cf = CodeFormat.objects.create(
        name=V2_ADMIN_FORMAT_NAME, separator="*", code_version=3)
    CodeComponent.objects.create(
        code_format=cf, ordering=0, name="code_id", hash_format="S",
        hash_algorithm="noop", hash_len=6, max_parts=1)
    for i, (name, max_parts) in enumerate(ADMIN_FLAG_COMPONENTS, start=1):
        CodeComponent.objects.create(
            code_format=cf, ordering=i, name=name, hash_format="S",
            hash_algorithm="noop", hash_len=3, max_parts=max_parts)


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0021_competitor_code_format_v2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeformat',
            name='code_version',
            field=models.PositiveSmallIntegerField(choices=[(1, 'legacy (hash components)'), (2, 'v2 (fixed length, signed, check character)'), (3, 'v2 administrator code (17 characters)')], default=1),
        ),
        migrations.RunPython(create_v2_admin_format,
                             migrations.RunPython.noop),
    ]
