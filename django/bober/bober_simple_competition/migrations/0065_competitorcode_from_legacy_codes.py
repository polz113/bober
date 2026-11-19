from django.db import migrations

# resume_attempt is not migrated: resuming attempts was removed in favour
# of merging attempts (Attempt.merge()).
PRIVILEGES = ('attempt', 'attempt_before_start', 'results_before_end')
BATCH_SIZE = 1000


def legacy_codes_to_competitor_codes(apps, schema_editor):
    """Create a CompetitorCode row for every competitor code issued so far.

    Older codes store their questionset as the prefix of the code value
    ("<cqs id>-<questionset slug><separator>...") and their privileges in
    CodePart rows. The rest of the value (what competitors type) becomes
    CompetitorCode.value, exactly as stored, so these codes keep working
    when typed as issued.

    Only adds rows; Code and CodePart rows are not changed. Codes whose
    value does not start with the prefix of a questionset of their
    competition, and second codes with the same value in one questionset,
    are skipped.
    """
    CompetitionQuestionSet = apps.get_model(
        'bober_simple_competition', 'CompetitionQuestionSet')
    CompetitorCode = apps.get_model(
        'bober_simple_competition', 'CompetitorCode')
    Code = apps.get_model('code_based_auth', 'Code')
    CodePart = apps.get_model('code_based_auth', 'CodePart')
    cqs_list = CompetitionQuestionSet.objects.select_related(
        'questionset', 'competition__competitor_code_generator__format')
    for cqs in cqs_list.iterator():
        generator = cqs.competition.competitor_code_generator
        prefix = (str(cqs.id) + '-' + cqs.questionset.slug
                  + generator.format.separator)
        code_ids = set(generator.codes.filter(
            value__startswith=prefix).values_list('id', flat=True))
        if cqs.guest_code_id is not None:
            code_ids.add(cqs.guest_code_id)
        code_ids -= set(CompetitorCode.objects.filter(
            code_id__in=code_ids).values_list('code_id', flat=True))
        seen = set(CompetitorCode.objects.filter(
            competition_questionset=cqs).values_list('value', flat=True))
        code_ids = sorted(code_ids)
        for start in range(0, len(code_ids), BATCH_SIZE):
            batch = code_ids[start:start + BATCH_SIZE]
            privileges = {}
            for code_id, value in CodePart.objects.filter(
                    code_id__in=batch,
                    name='competitor_privileges').values_list(
                        'code_id', 'value'):
                privileges.setdefault(code_id, set()).add(value)
            new_rows = []
            for code_id, value in Code.objects.filter(
                    id__in=batch).order_by('id').values_list('id', 'value'):
                if not value.startswith(prefix):
                    continue
                short_value = value[len(prefix):]
                if not short_value or short_value in seen:
                    continue
                seen.add(short_value)
                flags = privileges.get(code_id, set())
                new_rows.append(CompetitorCode(
                    code_id=code_id, competition_questionset=cqs,
                    value=short_value,
                    **dict((p, p in flags) for p in PRIVILEGES)))
            CompetitorCode.objects.bulk_create(new_rows)


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0064_competitorcode'),
        ('code_based_auth', '0019_alter_codecomponent_hash_algorithm'),
    ]

    operations = [
        migrations.RunPython(legacy_codes_to_competitor_codes,
                             migrations.RunPython.noop),
    ]
