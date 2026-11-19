import datetime
import importlib
from unittest import mock

from django.apps import apps
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils import timezone

from code_based_auth import random_code
from code_based_auth.models import CodeFormat, CodeGenerator
from bober_simple_competition import views
from bober_simple_competition.forms import (
    WRONG_CODE_MESSAGE, CompetitionCompetitorForm,
    CompetitionQuestionSetUpdateForm, QuestionSetCompetitorForm,
    QuestionSetRegistrationForm,
)
from bober_simple_competition.models import (
    Competition, CompetitionQuestionSet, CompetitorCode, QuestionSet,
)

legacy_migration = importlib.import_module(
    'bober_simple_competition.migrations.'
    '0065_competitorcode_from_legacy_codes')


def legacy_competitor_format():
    # as created by CompetitorCodeFormatCreate
    return CodeFormat.from_components([
        {'name': 'competition_questionset', 'hash_len': 64,
         'hash_format': 'r', 'hash_algorithm': 'noop', 'max_parts': 1},
        {'name': 'code_id', 'hash_len': 8, 'hash_format': 'h',
         'hash_algorithm': 'noop', 'max_parts': 1},
        {'name': 'competitor_privileges', 'hash_len': 3, 'hash_format': 'h',
         'hash_algorithm': 'sha512', 'max_parts': 4},
    ])


class CompetitorCodeTestMixin(object):
    def make_competition(self, slug, start_offset=-1):
        admin_format = CodeFormat.from_components([
            {'name': 'code_id', 'hash_len': 8, 'hash_format': 'h',
             'hash_algorithm': 'noop', 'max_parts': 1},
            {'name': 'admin_privileges', 'hash_len': 3, 'hash_format': 'h',
             'hash_algorithm': 'sha512', 'max_parts': 10},
        ])
        now = timezone.now()
        competition = Competition.objects.create(
            slug=slug,
            administrator_code_generator=CodeGenerator.objects.create(
                unique_code_component='code_id', format=admin_format,
                salt='adminsalt'),
            competitor_code_generator=CodeGenerator.objects.create(
                unique_code_component='code_id',
                format=legacy_competitor_format(), salt='competitorsalt'),
            start=now + datetime.timedelta(hours=start_offset),
            end=now + datetime.timedelta(hours=2))
        groups = []
        for name in ('mlajsi', 'starejsi'):
            qs = QuestionSet.objects.create(slug=slug + '-' + name, name=name)
            groups.append(CompetitionQuestionSet.objects.create(
                name=name, questionset=qs, competition=competition))
        return competition, groups

    def make_code(self, cqs, privileges=('attempt',)):
        code = cqs.competition.competitor_code_create(
            None, competition_questionset=cqs,
            code_data={'competitor_privileges': list(privileges)})
        return code, code.competitor_code

    def form_data(self, short_code, **kwargs):
        data = {
            'first_name': 'Ana', 'last_name': 'Novak',
            'date_of_birth_0': '1', 'date_of_birth_1': '2',
            'date_of_birth_2': '2015',
            'short_access_code': short_code,
        }
        data.update(kwargs)
        return data


class CompetitorCodeCreateTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        self.competition, (self.cqs, self.other_cqs) = \
            self.make_competition('create-test')

    def test_create_stores_random_code(self):
        code, cc = self.make_code(
            self.cqs, ('attempt', 'resume_attempt'))
        self.assertEqual(random_code.canonical(cc.value), cc.value)
        self.assertEqual(code.value, self.cqs.slug_str() + '*' + cc.value)
        self.assertEqual(cc.competition_questionset, self.cqs)
        self.assertEqual(cc.privileges, ['attempt', 'resume_attempt'])
        self.assertTrue(self.competition.competitor_code_generator.codes
                        .filter(id=code.id).exists())
        self.assertEqual(code.parts['competitor_privileges'],
                         ['attempt', 'resume_attempt'])

    def test_values_are_unique_per_questionset(self):
        values = [self.make_code(self.cqs)[1].value for _ in range(200)]
        self.assertEqual(len(set(values)), 200)

    def test_create_retries_on_collision(self):
        taken = self.make_code(self.cqs)[1].value
        with mock.patch.object(random_code, 'generate',
                               side_effect=[taken, 'AAAAA-BBBBB']):
            code, cc = self.make_code(self.cqs)
        self.assertEqual(cc.value, 'AAAAA-BBBBB')
        self.assertEqual(
            CompetitorCode.objects.filter(value=taken).count(), 1)

    def test_same_value_in_other_questionset(self):
        taken = self.make_code(self.cqs)[1].value
        with mock.patch.object(random_code, 'generate',
                               return_value=taken):
            code, cc = self.make_code(self.other_cqs)
        self.assertEqual(cc.value, taken)

    def test_create_gives_up(self):
        taken = self.make_code(self.cqs)[1].value
        with mock.patch.object(random_code, 'generate',
                               return_value=taken):
            with self.assertRaises(RuntimeError):
                self.make_code(self.cqs)

    def test_create_refuses_other_competition(self):
        other, (other_cqs, _) = self.make_competition('other-competition')
        with self.assertRaises(ValueError):
            self.competition.competitor_code_create(
                None, other_cqs, {'competitor_privileges': ['attempt']})


class CompetitorCodeCheckTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        self.competition, (self.cqs, self.other_cqs) = \
            self.make_competition('check-test')
        self.code, self.cc = self.make_code(self.cqs)
        self.raw = self.cc.value.replace('-', '')

    def test_lookup_normalizes_input(self):
        for typed in (self.cc.value, self.raw.lower(),
                      self.raw[:3] + ' ' + self.raw[3:],
                      self.raw.replace('0', 'o').replace('1', 'l')):
            self.assertEqual(CompetitorCode.lookup(self.cqs, typed),
                             self.cc, typed)

    def test_code_of_other_group_is_rejected(self):
        self.assertIsNone(CompetitorCode.lookup(self.other_cqs, self.raw))
        self.assertIsNone(CompetitorCode.from_access_code(
            self.other_cqs, self.code.value))
        form = CompetitionCompetitorForm(
            self.form_data(self.raw,
                           competition_questionset=self.other_cqs.id),
            competition=self.competition)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['short_access_code'],
                         [str(WRONG_CODE_MESSAGE)])

    def test_unknown_code_single_message(self):
        for typed in ('AAAAA-AAAAA', 'nonsense', self.raw[:-1]):
            form = QuestionSetCompetitorForm(
                self.form_data(typed), competitionquestionset=self.cqs)
            self.assertFalse(form.is_valid())
            self.assertEqual(form.errors['short_access_code'],
                             [str(WRONG_CODE_MESSAGE)])

    def test_questionset_form_stores_canonical_code(self):
        form = QuestionSetCompetitorForm(
            self.form_data(self.raw.lower()),
            competitionquestionset=self.cqs)
        self.assertTrue(form.is_valid(), form.errors)
        # this ends up in the session and in Attempt.access_code
        self.assertEqual(form.cleaned_data['full_code'], self.code.value)

    def test_competition_form_stores_canonical_code(self):
        form = CompetitionCompetitorForm(
            self.form_data(self.raw.replace('0', 'O'),
                           competition_questionset=self.cqs.id),
            competition=self.competition)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['full_code'], self.code.value)

    def test_registration_form(self):
        form = QuestionSetRegistrationForm(
            {'first_name': 'Ana', 'last_name': 'Novak',
             'access_code': self.raw.lower()},
            competitionquestionset=self.cqs)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['full_code'], self.code.value)

    def test_privileges_are_read_from_the_row(self):
        form = QuestionSetCompetitorForm(
            self.form_data(self.raw), competitionquestionset=self.cqs)
        self.assertTrue(form.is_valid(), form.errors)
        CompetitorCode.objects.filter(id=self.cc.id).update(attempt=False)
        form = QuestionSetCompetitorForm(
            self.form_data(self.raw), competitionquestionset=self.cqs)
        self.assertFalse(form.is_valid())
        # resume_attempt drops the profile (look up attempts by code only)
        CompetitorCode.objects.filter(id=self.cc.id).update(
            attempt=True, resume_attempt=True)
        form = QuestionSetCompetitorForm(
            self.form_data(self.raw), competitionquestionset=self.cqs)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertIsNone(form.profile)

    def _request(self, access_code):
        request = RequestFactory().get('/')
        request.session = {'access_code': access_code}
        return request

    def test_can_attempt(self):
        self.assertTrue(views._can_attempt(
            self._request(self.code.value), self.cqs))
        self.assertFalse(views._can_attempt(
            self._request(self.code.value), self.other_cqs))
        other_code, _ = self.make_code(self.other_cqs)
        self.assertFalse(views._can_attempt(
            self._request(other_code.value), self.cqs))
        CompetitorCode.objects.filter(id=self.cc.id).update(attempt=False)
        self.assertFalse(views._can_attempt(
            self._request(self.code.value), self.cqs))

    def test_can_attempt_before_start(self):
        competition, (cqs, _) = self.make_competition('later', 1)
        code, cc = self.make_code(cqs)
        self.assertFalse(views._can_attempt(self._request(code.value), cqs))
        CompetitorCode.objects.filter(id=cc.id).update(
            attempt_before_start=True)
        self.assertTrue(views._can_attempt(self._request(code.value), cqs))

    def test_competition_lookup(self):
        self.assertEqual(self.competition.competitor_code(self.code.value),
                         self.cc)
        other, _ = self.make_competition('another')
        self.assertIsNone(other.competitor_code(self.code.value))
        self.assertIsNone(self.competition.competitor_code('garbage'))

    def test_access_code_view_stores_canonical_code(self):
        url = reverse('competitionquestionset_access_code', kwargs={
            'competition_questionset_id': self.cqs.id, 'url_next': '/x/'})
        self.client.get(url, {'access_code': self.raw.lower()})
        self.assertEqual(self.client.session['access_code'],
                         self.code.value)


class GuestCodeTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        self.competition, (self.cqs, _) = self.make_competition('guest-test')

    def test_guest_code_from_questionset_form(self):
        form = CompetitionQuestionSetUpdateForm(
            {'name': self.cqs.name, 'questionset': self.cqs.questionset.id,
             'competition': self.competition.id,
             'guest_privileges': ['attempt', 'results_before_end']},
            instance=self.cqs)
        self.assertTrue(form.is_valid(), form.errors)
        form.save()
        self.cqs.refresh_from_db()
        cc = self.cqs.guest_code.competitor_code
        self.assertEqual(cc.privileges, ['attempt', 'results_before_end'])
        form = CompetitionQuestionSetUpdateForm(instance=self.cqs)
        self.assertEqual(form.fields['guest_privileges'].initial,
                         ['attempt', 'results_before_end'])
        # an empty code means the guest code
        form = QuestionSetCompetitorForm(
            self.form_data(''), competitionquestionset=self.cqs)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['full_code'],
                         self.cqs.guest_code.value)

    def test_no_guest_code(self):
        form = QuestionSetCompetitorForm(
            self.form_data(''), competitionquestionset=self.cqs)
        self.assertFalse(form.is_valid())


class LegacyCodeMigrationTest(CompetitorCodeTestMixin, TestCase):
    """Codes issued before random codes, migrated by migration 0065."""

    def setUp(self):
        self.competition, (self.cqs, self.other_cqs) = \
            self.make_competition('legacy-test')
        self.codegen = self.competition.competitor_code_generator
        self.legacy = self.codegen.create_code({
            'competition_questionset': [self.cqs.slug_str()],
            'competitor_privileges': ['attempt', 'resume_attempt'],
        })
        self.legacy_short = self.legacy.value[len(self.cqs.slug_str()) + 1:]
        self.assertFalse(CompetitorCode.objects.filter(
            code=self.legacy).exists())

    def migrate(self):
        legacy_migration.legacy_codes_to_competitor_codes(apps, None)

    def test_migration_fills_new_fields(self):
        self.migrate()
        cc = self.legacy.competitor_code
        self.assertEqual(cc.competition_questionset, self.cqs)
        self.assertEqual(cc.value, self.legacy_short)
        self.assertEqual(cc.privileges, ['attempt', 'resume_attempt'])
        # Code and CodePart rows are untouched
        self.legacy.refresh_from_db()
        self.assertEqual(self.legacy.value,
                         self.cqs.slug_str() + '*' + self.legacy_short)

    def test_migration_is_repeatable_and_skips_new_codes(self):
        self.make_code(self.cqs)
        self.migrate()
        self.migrate()
        self.assertEqual(CompetitorCode.objects.count(), 2)

    def test_migrated_code_works_in_exact_form(self):
        self.migrate()
        form = QuestionSetCompetitorForm(
            self.form_data(self.legacy_short),
            competitionquestionset=self.cqs)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['full_code'], self.legacy.value)
        request = RequestFactory().get('/')
        request.session = {'access_code': self.legacy.value}
        self.assertTrue(views._can_attempt(request, self.cqs))
        self.assertFalse(views._can_attempt(request, self.other_cqs))
        # only the exact form
        form = QuestionSetCompetitorForm(
            self.form_data(self.legacy_short.upper()),
            competitionquestionset=self.cqs)
        self.assertFalse(form.is_valid())

    def test_migration_skips_foreign_values(self):
        stray = self.codegen.create_code({
            'competition_questionset': ['999-nope'],
            'competitor_privileges': ['attempt'],
        })
        self.migrate()
        self.assertFalse(CompetitorCode.objects.filter(code=stray).exists())

    def test_migration_includes_guest_code(self):
        guest = self.codegen.create_code({
            'competition_questionset': [self.other_cqs.slug_str()],
            'competitor_privileges': ['attempt', 'results_before_end'],
        })
        self.codegen.codes.remove(guest)
        self.other_cqs.guest_code = guest
        self.other_cqs.save()
        self.migrate()
        self.assertEqual(guest.competitor_code.privileges,
                         ['attempt', 'results_before_end'])
