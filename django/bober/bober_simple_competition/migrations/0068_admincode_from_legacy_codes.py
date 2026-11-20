from django.db import migrations

# kind of privilege -> {privilege name: AdminCode field}, as in models.py
ADMIN_CODE_FIELDS = {
    'admin_privileges': dict((p, p) for p in (
        'create_admin_codes', 'create_competitor_codes', 'view_all_attempts',
        'view_all_admin_codes', 'view_all_competitor_codes',
        'use_question_sets', 'modify_competition', 'use_questions')),
    'competitor_privileges': dict((p, 'competitor_' + p) for p in (
        'attempt', 'attempt_before_start', 'results_before_end')),
    'allowed_effects': dict((e, 'allow_' + e) for e in (
        'let_manage', 'let_manage_recursive')),
}
BATCH_SIZE = 1000


def legacy_codes_to_admin_codes(apps, schema_editor):
    """Create an AdminCode row for every administrator code issued so far.

    Older administrator codes store their privileges in CodePart rows; the
    value is kept exactly as stored, so these codes keep working when typed
    as issued. Only adds rows; Code and CodePart rows are not changed. A
    second code with the same value in one competition is skipped.
    """
    Competition = apps.get_model('bober_simple_competition', 'Competition')
    AdminCode = apps.get_model('bober_simple_competition', 'AdminCode')
    Code = apps.get_model('code_based_auth', 'Code')
    CodePart = apps.get_model('code_based_auth', 'CodePart')
    for competition in Competition.objects.select_related(
            'administrator_code_generator').iterator():
        generator = competition.administrator_code_generator
        code_ids = set(generator.codes.values_list('id', flat=True))
        code_ids -= set(AdminCode.objects.filter(
            code_id__in=code_ids).values_list('code_id', flat=True))
        seen = set(AdminCode.objects.filter(
            competition=competition).values_list('value', flat=True))
        code_ids = sorted(code_ids)
        for start in range(0, len(code_ids), BATCH_SIZE):
            batch = code_ids[start:start + BATCH_SIZE]
            parts = {}
            for code_id, name, value in CodePart.objects.filter(
                    code_id__in=batch,
                    name__in=list(ADMIN_CODE_FIELDS)).values_list(
                        'code_id', 'name', 'value'):
                parts.setdefault(code_id, set()).add((name, value))
            new_rows = []
            for code_id, value in Code.objects.filter(
                    id__in=batch).order_by('id').values_list('id', 'value'):
                if not value or value in seen:
                    continue
                seen.add(value)
                given = parts.get(code_id, set())
                flags = {}
                for kind, fields in ADMIN_CODE_FIELDS.items():
                    for name, field in fields.items():
                        flags[field] = (kind, name) in given
                new_rows.append(AdminCode(
                    code_id=code_id, competition=competition, value=value,
                    **flags))
            AdminCode.objects.bulk_create(new_rows)


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0067_admincode'),
        ('code_based_auth', '0019_alter_codecomponent_hash_algorithm'),
    ]

    operations = [
        migrations.RunPython(legacy_codes_to_admin_codes,
                             migrations.RunPython.noop),
    ]
