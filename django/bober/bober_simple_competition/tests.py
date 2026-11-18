import datetime

from django.core.cache import cache
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from code_based_auth import code_v2
from code_based_auth.models import (
    CODE_ERROR_MESSAGES, CodeFormat, CodeGenerator,
)
from bober_simple_competition.forms import (
    CompetitionCompetitorForm, QuestionSetCompetitorForm,
)
from bober_simple_competition.models import (
    Competition, CompetitionQuestionSet, QuestionSet,
)


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
    def make_competition(self, competitor_format, slug):
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
                salt='adminsalt1'),
            competitor_code_generator=CodeGenerator.objects.create(
                unique_code_component='code_id', format=competitor_format,
                salt='0123456789abcdef0123456789abcdef'),
            start=now - datetime.timedelta(hours=1),
            end=now + datetime.timedelta(hours=1))
        groups = []
        for name in ('mlajsi', 'starejsi'):
            qs = QuestionSet.objects.create(slug=slug + '-' + name, name=name)
            groups.append(CompetitionQuestionSet.objects.create(
                name=name, questionset=qs, competition=competition))
        return competition, groups

    def form_data(self, short_code, **kwargs):
        data = {
            'first_name': 'Ana', 'last_name': 'Novak',
            'date_of_birth_0': '1', 'date_of_birth_1': '2',
            'date_of_birth_2': '2015',
            'short_access_code': short_code,
        }
        data.update(kwargs)
        return data


class V2CompetitorCodeTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        self.competition, (self.cqs, self.other_cqs) = self.make_competition(
            CodeFormat.create_v2(), 'v2-test')
        self.code = self.competition.competitor_code_create(
            None, competition_questionset=self.cqs,
            code_data={'competitor_privileges': ['attempt']})
        self.short = self.competition.split_competitor_code(
            self.code.value)[1]

    def test_competitor_code_create(self):
        self.assertEqual(self.code.value,
                         self.cqs.slug_str() + '*' + self.short)
        self.assertEqual(code_v2.canonical(self.short), self.short)

    def test_expand_competitor_code(self):
        codegen = self.competition.competitor_code_generator
        typed = self.short.lower().replace('-', '')
        full = self.competition.expand_competitor_code(typed, self.cqs)
        self.assertTrue(codegen.code_matches(
            full, {'competitor_privileges': ['attempt']}))
        self.assertTrue(codegen.code_matches(
            full, {'competition_questionset': [self.cqs.slug_str()]}))
        self.assertEqual(codegen.canonical_code(full), self.code.value)

    def test_questionset_form_stores_canonical_code(self):
        form = QuestionSetCompetitorForm(
            self.form_data(self.short.lower().replace('-', ' ')),
            competitionquestionset=self.cqs)
        self.assertTrue(form.is_valid(), form.errors)
        # this ends up in the session and in Attempt.access_code
        self.assertEqual(form.cleaned_data['full_code'], self.code.value)

    def test_competition_form_stores_canonical_code(self):
        form = CompetitionCompetitorForm(
            self.form_data(self.short.replace('0', 'O').replace('-', ''),
                           competition_questionset=self.cqs.id),
            competition=self.competition)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['full_code'], self.code.value)

    def test_competition_form_wrong_group(self):
        form = CompetitionCompetitorForm(
            self.form_data(self.short,
                           competition_questionset=self.other_cqs.id),
            competition=self.competition)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['short_access_code'],
            [str(CODE_ERROR_MESSAGES[code_v2.CodeSignatureError])])

    def test_questionset_form_typo_and_format_errors(self):
        raw = self.short.replace('-', '')
        typo = raw[:-1] + ('0' if raw[-1] != '0' else '1')
        for typed, error in ((typo, code_v2.CodeChecksumError),
                             (raw[:10], code_v2.InvalidCodeFormat)):
            form = QuestionSetCompetitorForm(
                self.form_data(typed), competitionquestionset=self.cqs)
            self.assertFalse(form.is_valid())
            self.assertEqual(form.errors['short_access_code'],
                             [str(CODE_ERROR_MESSAGES[error])])

    def test_code_without_attempt_privilege_is_rejected(self):
        code = self.competition.competitor_code_create(
            None, competition_questionset=self.cqs,
            code_data={'competitor_privileges': ['results_before_end']})
        short = self.competition.split_competitor_code(code.value)[1]
        form = QuestionSetCompetitorForm(
            self.form_data(short), competitionquestionset=self.cqs)
        self.assertFalse(form.is_valid())


class LegacyCompetitorCodeTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        self.competition, (self.cqs, self.other_cqs) = self.make_competition(
            legacy_competitor_format(), 'legacy-test')
        self.code = self.competition.competitor_code_create(
            None, competition_questionset=self.cqs,
            code_data={'competitor_privileges': ['attempt']})
        self.short = '*'.join(self.competition.split_competitor_code(
            self.code.value)[1:])

    def test_questionset_form(self):
        form = QuestionSetCompetitorForm(
            self.form_data(self.short.upper()),
            competitionquestionset=self.cqs)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['full_code'], self.code.value)

    def test_competition_form_wrong_group(self):
        form = CompetitionCompetitorForm(
            self.form_data(self.short,
                           competition_questionset=self.other_cqs.id),
            competition=self.competition)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['short_access_code'],
                         ['Wrong access code'])


@override_settings(CODE_AUTH_MAX_FAILURES=3, CODE_AUTH_FAILURE_WINDOW=60)
class AccessCodeThrottleTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        cache.clear()
        self.competition, (self.cqs, self.other_cqs) = self.make_competition(
            CodeFormat.create_v2(), 'throttle-test')
        self.code = self.competition.competitor_code_create(
            None, competition_questionset=self.cqs,
            code_data={'competitor_privileges': ['attempt']})
        self.short = self.competition.split_competitor_code(
            self.code.value)[1]
        self.url = reverse('questionset_compete', kwargs={
            'competition_questionset_id': self.cqs.id})

    def tearDown(self):
        cache.clear()

    def post(self, short_code, ip='10.0.0.1'):
        return self.client.post(self.url, self.form_data(short_code),
                                REMOTE_ADDR=ip)

    def test_wrong_codes_are_throttled(self):
        wrong = self.short[:-1] + ('0' if self.short[-1] != '0' else '1')
        for _ in range(3):
            response = self.post(wrong)
            self.assertNotEqual(response.status_code, 429)
        self.assertEqual(self.post(wrong).status_code, 429)
        # also a correct code is refused while throttled
        self.assertEqual(self.post(self.short).status_code, 429)
        # other clients are not affected
        response = self.post(self.short, ip='10.0.0.2')
        self.assertEqual(response.status_code, 302)

    def test_correct_codes_are_not_counted(self):
        for _ in range(5):
            self.client.logout()
            response = self.post(self.short)
            self.assertEqual(response.status_code, 302)

    def test_access_code_view_counts_typed_wrong_codes(self):
        url = reverse('competitionquestionset_access_code', kwargs={
            'competition_questionset_id': self.cqs.id, 'url_next': 'done/'})
        for _ in range(3):
            response = self.client.get(url, {'access_code': 'WRONG'},
                                       REMOTE_ADDR='10.0.0.3')
            self.assertEqual(response.status_code, 302)
        response = self.client.get(url, {'access_code': self.short},
                                   REMOTE_ADDR='10.0.0.3')
        self.assertEqual(response.status_code, 429)
