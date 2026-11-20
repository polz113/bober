import datetime
import importlib
from unittest import mock

from django.apps import apps
from django.core.cache import cache
from django.test import RequestFactory, TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from code_based_auth import random_code
from code_based_auth.models import Code, CodeFormat, CodeGenerator, CodePart
from bober_simple_competition import views
from bober_simple_competition.forms import (
    WRONG_CODE_MESSAGE, CompetitionCompetitorForm,
    CompetitionQuestionSetUpdateForm, QuestionSetCompetitorForm,
    QuestionSetRegistrationForm,
)
from django.contrib.auth.models import User
from bober_simple_competition.models import (
    ADMIN_PRIVILEGES, CODE_EFFECTS, COMPETITOR_PRIVILEGES, AdminCode,
    Answer, Attempt, AttemptConfirmation, Competition, MergeError, CompetitionQuestionSet, CompetitorCode,
    Question, QuestionSet,
)

legacy_migration = importlib.import_module(
    'bober_simple_competition.migrations.'
    '0065_competitorcode_from_legacy_codes')


def legacy_code(generator, value, parts):
    """Store a code the way codes were stored before random codes: the
    value, the privileges as CodeParts, and the code in its generator."""
    code = Code.objects.create(value=value, salt=generator.salt,
                               format=generator.format)
    for name, values in parts.items():
        for i, v in enumerate(values):
            CodePart.objects.create(code=code, ordering=i, name=name, value=v)
    generator.codes.add(code)
    return code


class CompetitorCodeTestMixin(object):
    def make_competition(self, slug, start_offset=-1, legacy=False):
        """A competition; legacy: created before random codes (its code
        generators have a code format and a salt)."""
        if legacy:
            generators = [CodeGenerator.objects.create(
                unique_code_component='code_id', salt=salt,
                format=CodeFormat.objects.create(separator='*'))
                for salt in ('adminsalt', 'competitorsalt')]
        else:
            generators = [CodeGenerator.objects.create(),
                          CodeGenerator.objects.create()]
        now = timezone.now()
        competition = Competition.objects.create(
            slug=slug,
            administrator_code_generator=generators[0],
            competitor_code_generator=generators[1],
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
            self.cqs, ('attempt', 'results_before_end'))
        self.assertEqual(random_code.canonical(cc.value), cc.value)
        self.assertEqual(code.value, self.cqs.slug_str() + '*' + cc.value)
        self.assertEqual(cc.competition_questionset, self.cqs)
        self.assertEqual(cc.privileges, ['attempt', 'results_before_end'])
        self.assertTrue(self.competition.competitor_code_generator.codes
                        .filter(id=code.id).exists())
        # privileges live in the row, not in CodeParts
        self.assertEqual(code.parts, {})

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
             'competition': self.competition.id, 'code_length': 10,
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
            self.make_competition('legacy-test', legacy=True)
        self.codegen = self.competition.competitor_code_generator
        self.legacy = legacy_code(
            self.codegen, self.cqs.slug_str() + '*0000002a*f3c+a01', {
                'competition_questionset': [self.cqs.slug_str()],
                'competitor_privileges': ['attempt', 'results_before_end'],
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
        self.assertEqual(cc.privileges, ['attempt', 'results_before_end'])
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
        stray = legacy_code(self.codegen, '999-nope*0000002b*f3c', {
            'competition_questionset': ['999-nope'],
            'competitor_privileges': ['attempt'],
        })
        self.migrate()
        self.assertFalse(CompetitorCode.objects.filter(code=stray).exists())

    def test_migration_includes_guest_code(self):
        guest = legacy_code(
            self.codegen, self.other_cqs.slug_str() + '*0000002c*a01', {
                'competition_questionset': [self.other_cqs.slug_str()],
                'competitor_privileges': ['attempt', 'results_before_end'],
            })
        self.codegen.codes.remove(guest)
        self.other_cqs.guest_code = guest
        self.other_cqs.save()
        self.migrate()
        self.assertEqual(guest.competitor_code.privileges,
                         ['attempt', 'results_before_end'])


@override_settings(CODE_AUTH_MAX_FAILURES=3)
class AccessCodeThrottleTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        cache.clear()
        self.competition, (self.cqs, self.other_cqs) = \
            self.make_competition('throttle-test')
        self.code, self.cc = self.make_code(self.cqs)
        self.short = self.cc.value
        self.url = reverse('questionset_compete', kwargs={
            'competition_questionset_id': self.cqs.id})

    def tearDown(self):
        cache.clear()

    def post(self, short_code, ip='10.0.0.1'):
        return self.client.post(self.url, self.form_data(short_code),
                                REMOTE_ADDR=ip)

    def wrong_code(self):
        return self.short[:-1] + ('0' if self.short[-1] != '0' else '1')

    def test_wrong_codes_are_throttled(self):
        for _ in range(3):
            response = self.post(self.wrong_code())
            self.assertNotEqual(response.status_code, 429)
        self.assertEqual(self.post(self.wrong_code()).status_code, 429)
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

    def test_code_of_other_group_is_counted(self):
        other_code, other_cc = self.make_code(self.other_cqs)
        for _ in range(3):
            self.post(other_cc.value)
        self.assertEqual(self.post(self.short).status_code, 429)

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


@override_settings(CODE_AUTH_MAX_FAILURES=3)
class AccessCodePageThrottleTest(CompetitorCodeTestMixin, TestCase):
    """The generic access code page, where admin codes are typed."""

    def setUp(self):
        cache.clear()
        self.competition, _groups = self.make_competition(
            'admin-throttle-test')
        self.master = self.competition.master_code_create()
        self.url = reverse('access_code', kwargs={'url_next': 'done/'})

    def tearDown(self):
        cache.clear()

    def enter(self, code, ip='10.0.1.1'):
        return self.client.get(self.url, {'access_code': code},
                               REMOTE_ADDR=ip)

    def test_correct_codes_are_not_counted(self):
        for _ in range(5):
            self.assertEqual(self.enter(self.master.value).status_code, 302)
        self.assertEqual(self.client.session['access_code'],
                         self.master.value)

    def test_wrong_codes_are_throttled(self):
        for _ in range(3):
            self.assertEqual(
                self.enter(self.master.value + 'x').status_code, 302)
        self.assertEqual(self.enter(self.master.value + 'x').status_code, 429)
        # a correct code is refused too while throttled ...
        self.assertEqual(self.enter(self.master.value).status_code, 429)
        # ... but only for this client
        self.assertEqual(
            self.enter(self.master.value, ip='10.0.1.2').status_code, 302)


class FakeGraders(object):
    """Grades 'ok' with 1 and anything else with -1; records the seeds."""
    def __init__(self):
        self.seeds = []

    def get_grader(self, function, function_type):
        def grade(value, seed, question):
            self.seeds.append(seed)
            return 1.0 if value == 'ok' else -1.0
        return grade


class AttemptMergeTestMixin(CompetitorCodeTestMixin):
    def setUp(self):
        self.graders = FakeGraders()
        patcher = mock.patch(
            'bober_simple_competition.graders.init_runtimes',
            side_effect=lambda m=None: m or self.graders)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.competition, (self.cqs, self.other_cqs) = \
            self.make_competition('merge-test')
        self.questions = []
        for i in range(3):
            q = Question.objects.create(
                country='si', slug='q%d' % i, identifier='q%d' % i,
                title='Q%d' % i, language='sl')
            self.cqs.questionset.questions.add(q)
            self.other_cqs.questionset.questions.add(q)
            self.questions.append(q)
        self.code, _ = self.make_code(self.cqs)

    def attempt(self, answers, cqs=None, seed=None, code=None):
        """answers: list of (question index, value), oldest first."""
        cqs = cqs or self.cqs
        a = Attempt.objects.create(
            competitionquestionset=cqs,
            access_code=(code or self.code).value,
            random_seed=seed if seed is not None else len(
                Attempt.objects.all()) + 11,
            finish=timezone.now() + datetime.timedelta(hours=1))
        mapping = cqs.questionset.question_mapping(a.random_seed)
        for i, value in answers:
            Answer.objects.create(
                attempt=a, value=value,
                randomized_question_id=mapping[self.questions[i].identifier])
        a.regrade()
        return a

    def graded(self, attempt):
        return dict((g.question_id, (g.answer.attempt_id, g.score))
                    for g in attempt.gradedanswer_set.all())


class AttemptMergeTest(AttemptMergeTestMixin, TestCase):
    def test_merge_counts_latest_answers_of_all_attempts(self):
        first = self.attempt([(0, 'ok'), (1, 'bad')])
        second = self.attempt([(1, 'ok'), (2, 'bad')])
        first.merge([second])
        second.refresh_from_db()
        self.assertEqual(second.merged_into, first)
        q0, q1, q2 = [q.id for q in self.questions]
        self.assertEqual(self.graded(first), {
            q0: (first.id, 1.0), q1: (second.id, 1.0),
            q2: (second.id, -1.0)})

    def test_answers_are_graded_with_their_own_seed(self):
        first = self.attempt([(0, 'ok')], seed=101)
        second = self.attempt([(1, 'ok')], seed=202)
        self.graders.seeds = []
        first.merge([second])
        self.assertEqual(sorted(self.graders.seeds), [101, 202])

    def test_split_restores_the_original_attempts(self):
        first = self.attempt([(0, 'ok'), (1, 'bad')])
        second = self.attempt([(1, 'ok')])
        before = (self.graded(first), self.graded(second))
        first.merge([second])
        parts = first.split()
        self.assertEqual([p.id for p in parts], [second.id])
        second.refresh_from_db()
        self.assertIsNone(second.merged_into)
        self.assertEqual((self.graded(first), self.graded(second)), before)

    def test_score_is_updated_if_it_was_set(self):
        first = self.attempt([(0, 'ok')])
        second = self.attempt([(1, 'ok')])
        Attempt.objects.filter(id=first.id).update(score=1)
        first.refresh_from_db()
        first.merge([second])
        self.assertEqual(first.score, 2)
        first.split()
        self.assertEqual(first.score, 1)

    def test_merge_moves_earlier_merges(self):
        a, b, c = [self.attempt([(i, 'ok')]) for i in range(3)]
        b.merge([c])
        a.merge([b])
        self.assertEqual(sorted(Attempt.objects.filter(
            merged_into=a).values_list('id', flat=True)), [b.id, c.id])
        self.assertEqual(len(self.graded(a)), 3)
        a.split()
        self.assertFalse(Attempt.objects.filter(
            merged_into__isnull=False).exists())

    def test_merge_refuses_other_questionset_and_merged(self):
        first = self.attempt([(0, 'ok')])
        other = self.attempt([(0, 'ok')], cqs=self.other_cqs)
        with self.assertRaises(ValueError):
            first.merge([other])
        second = self.attempt([(1, 'ok')])
        first.merge([second])
        second.refresh_from_db()
        third = self.attempt([(2, 'ok')])
        with self.assertRaises(ValueError):
            second.merge([third])
        with self.assertRaises(ValueError):
            third.merge([second])

    def test_questionset_regrade_keeps_merges(self):
        first = self.attempt([(0, 'ok')])
        second = self.attempt([(1, 'ok'), (0, 'bad')])
        first.merge([second])
        expected = self.graded(first)
        self.cqs.grade_answers(update_graded=True, regrade=True)
        self.assertEqual(self.graded(first), expected)
        self.assertEqual(self.graded(second), {})


class AttemptMergeViewTest(AttemptMergeTestMixin, TestCase):
    def setUp(self):
        super(AttemptMergeViewTest, self).setUp()
        self.teacher = User.objects.create_user('teacher', password='pw')
        self.teacher.profile.created_codes.add(self.code)
        self.other = User.objects.create_user('other', password='pw')
        self.first = self.attempt([(0, 'ok')])
        self.second = self.attempt([(1, 'ok')])
        self.merge_url = reverse('attempt_merge', kwargs={
            'competition_questionset_id': self.cqs.id})

    def split_url(self, attempt):
        return reverse('attempt_split', kwargs={
            'competition_questionset_id': self.cqs.id,
            'attempt_id': attempt.id})

    def test_teacher_merges_and_splits(self):
        self.client.login(username='teacher', password='pw')
        response = self.client.post(
            self.merge_url,
            {'attempt_id': [self.second.id, self.first.id]})
        self.assertEqual(response.status_code, 200, response.content)
        self.second.refresh_from_db()
        # merged into the earliest attempt
        self.assertEqual(self.second.merged_into_id, self.first.id)
        self.assertEqual(self.second.merged_by, self.teacher.profile)
        # a merged attempt can not be confirmed
        response = self.client.post(reverse('attempt_confirm', kwargs={
            'competition_questionset_id': self.cqs.id,
            'attempt_id': self.second.id}))
        self.assertEqual(response.status_code, 400)
        response = self.client.post(self.split_url(self.first))
        self.assertEqual(response.status_code, 200, response.content)
        self.second.refresh_from_db()
        self.assertIsNone(self.second.merged_into)

    def test_only_the_teacher_can_merge(self):
        self.client.login(username='other', password='pw')
        response = self.client.post(
            self.merge_url, {'attempt_id': [self.first.id, self.second.id]})
        self.assertEqual(response.status_code, 403)
        self.first.merge([self.second])
        response = self.client.post(self.split_url(self.first))
        self.assertEqual(response.status_code, 403)
        self.second.refresh_from_db()
        self.assertEqual(self.second.merged_into_id, self.first.id)

    def test_teacher_needs_all_codes(self):
        foreign_code, _ = self.make_code(self.cqs)
        foreign = self.attempt([(2, 'ok')], code=foreign_code)
        self.client.login(username='teacher', password='pw')
        response = self.client.post(
            self.merge_url, {'attempt_id': [self.first.id, foreign.id]})
        self.assertEqual(response.status_code, 403)

    def test_attempts_of_other_questionset_are_refused(self):
        other_code, _ = self.make_code(self.other_cqs)
        self.teacher.profile.created_codes.add(other_code)
        other = self.attempt([(0, 'ok')], cqs=self.other_cqs,
                             code=other_code)
        self.client.login(username='teacher', password='pw')
        response = self.client.post(
            self.merge_url, {'attempt_id': [self.first.id, other.id]})
        self.assertEqual(response.status_code, 403)

    def test_needs_two_attempts(self):
        self.client.login(username='teacher', password='pw')
        response = self.client.post(
            self.merge_url, {'attempt_id': [self.first.id]})
        self.assertEqual(response.status_code, 400)


admin_migration = importlib.import_module(
    'bober_simple_competition.migrations.0068_admincode_from_legacy_codes')


class AdminCodeTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        self.competition, (self.cqs, _) = self.make_competition('admin-test')
        self.master = self.competition.master_code_create()
        self.admin_code = self.master.admin_code

    def test_master_code_has_everything(self):
        self.assertEqual(random_code.canonical(self.master.value),
                         self.master.value)
        self.assertEqual(self.admin_code.competition, self.competition)
        self.assertEqual(sorted(self.admin_code.privileges(
            'admin_privileges')), sorted(p for p, _ in ADMIN_PRIVILEGES))
        self.assertEqual(sorted(self.admin_code.privileges(
            'competitor_privileges')),
            sorted(p for p, _ in COMPETITOR_PRIVILEGES))
        self.assertEqual(sorted(self.admin_code.privileges(
            'allowed_effects')), sorted(e for e, _ in CODE_EFFECTS))
        self.assertTrue(self.competition.administrator_code_generator.codes
                        .filter(id=self.master.id).exists())
        self.assertEqual(list(self.competition.organizer_codes()),
                         [self.master])

    def test_lookup_normalizes_input(self):
        raw = self.master.value.replace('-', '')
        for typed in (self.master.value, raw.lower(),
                      raw.replace('0', 'o').replace('1', 'i')):
            self.assertEqual(self.competition.admin_code(typed),
                             self.admin_code, typed)
        self.assertIsNone(self.competition.admin_code('AAAAA-AAAAA'))
        self.assertIsNone(self.competition.admin_code(None))

    def test_code_of_other_competition_is_rejected(self):
        other, _ = self.make_competition('admin-other')
        self.assertIsNone(other.admin_code(self.master.value))
        self.assertFalse(other.admin_code_allows(
            self.master.value, 'admin_privileges', 'modify_competition'))

    def test_privileges_are_read_from_the_row(self):
        allows = self.competition.admin_code_allows
        self.assertTrue(allows(self.master.value, 'admin_privileges',
                               'modify_competition'))
        AdminCode.objects.filter(id=self.admin_code.id).update(
            modify_competition=False, competitor_attempt=False)
        self.assertFalse(allows(self.master.value, 'admin_privileges',
                                'modify_competition'))
        self.assertFalse(allows(self.master.value, 'competitor_privileges',
                                'attempt'))
        self.assertFalse(allows(self.master.value, 'admin_privileges',
                                'no_such_privilege'))

    def test_admin_code_create_defaults_to_own_privileges(self):
        AdminCode.objects.filter(id=self.admin_code.id).update(
            create_admin_codes=False, allow_let_manage=False)
        code = self.competition.admin_code_create(self.master.value)
        created = code.admin_code
        self.assertNotEqual(code.value, self.master.value)
        self.assertFalse(created.create_admin_codes)
        self.assertFalse(created.allow_let_manage)
        self.assertTrue(created.modify_competition)
        self.assertEqual(
            self.competition.max_competitor_code_data(self.master.value),
            {'competitor_privileges': [p for p, _ in COMPETITOR_PRIVILEGES]})

    def test_create_retries_on_collision(self):
        with mock.patch.object(random_code, 'generate',
                               side_effect=[self.master.value,
                                            'AAAAA-BBBBB']):
            code = self.competition.admin_code_create(
                None, {'admin_privileges': ['view_all_attempts']})
        self.assertEqual(code.value, 'AAAAA-BBBBB')
        self.assertEqual(code.admin_code.privileges('admin_privileges'),
                         ['view_all_attempts'])
        # the same value in another competition is fine
        other, _ = self.make_competition('admin-other')
        with mock.patch.object(random_code, 'generate',
                               return_value=self.master.value):
            code = other.master_code_create()
        self.assertEqual(code.value, self.master.value)

    def test_code_effects_are_stored(self):
        code = self.competition.admin_code_create(None, {
            'admin_privileges': [], 'code_effects': ['let_manage']})
        self.assertEqual(code.parts, {'code_effects': ['let_manage']})

    def test_access_code_page_stores_canonical_code(self):
        response = self.client.get(
            reverse('access_code', kwargs={'url_next': 'done/'}),
            {'access_code': self.master.value.replace('-', '').lower()})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['access_code'],
                         self.master.value)


class AdminCodeViewTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        self.competition, (self.cqs, _) = self.make_competition('admin-view')
        self.master = self.competition.master_code_create()
        self.user = User.objects.create_user('organizer', password='pw')
        self.client.login(username='organizer', password='pw')
        session = self.client.session
        session['access_code'] = self.master.value
        session.save()

    def test_create_admin_code_in_view(self):
        url = reverse('competition_code_create', kwargs={
            'slug': self.competition.slug, 'user_type': 'admin'})
        response = self.client.post(url, {
            'admin_privileges': ['view_all_attempts'],
            'competitor_privileges': ['attempt']})
        self.assertEqual(response.status_code, 302)
        code = self.user.profile.created_codes.get()
        self.assertEqual(code.admin_code.privileges('admin_privileges'),
                         ['view_all_attempts'])
        self.assertEqual(code.admin_code.privileges('competitor_privileges'),
                         ['attempt'])

    def test_create_competitor_code_in_view(self):
        url = reverse('competition_code_create', kwargs={
            'slug': self.competition.slug, 'user_type': 'competitor'})
        response = self.client.post(url, {
            'competitor_privileges': ['attempt'],
            'competition_questionset': self.cqs.id})
        self.assertEqual(response.status_code, 302)
        code = self.user.profile.created_codes.get()
        self.assertEqual(code.competitor_code.competition_questionset,
                         self.cqs)
        self.assertEqual(code.competitor_code.privileges, ['attempt'])

    def test_without_privilege(self):
        AdminCode.objects.filter(code=self.master).update(
            create_admin_codes=False)
        url = reverse('competition_code_create', kwargs={
            'slug': self.competition.slug, 'user_type': 'admin'})
        response = self.client.post(url, {
            'admin_privileges': ['view_all_attempts']})
        self.assertEqual(response.status_code, 403)


class LegacyAdminCodeMigrationTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        self.competition, _ = self.make_competition(
            'legacy-admin', legacy=True)
        # an administrator code as stored before random codes
        self.legacy = legacy_code(
            self.competition.administrator_code_generator,
            '0000002a*f3c+a01', {
                'admin_privileges': ['view_all_admin_codes',
                                     'create_competitor_codes'],
                'competitor_privileges': ['attempt', 'resume_attempt'],
                'allowed_effects': ['let_manage'],
            })

    def migrate(self):
        admin_migration.legacy_codes_to_admin_codes(apps, None)

    def test_migration_fills_new_fields(self):
        self.migrate()
        self.migrate()
        admin_code = self.legacy.admin_code
        self.assertEqual(admin_code.value, self.legacy.value)
        self.assertEqual(
            sorted(admin_code.privileges('admin_privileges')),
            ['create_competitor_codes', 'view_all_admin_codes'])
        self.assertEqual(admin_code.privileges('competitor_privileges'),
                         ['attempt'])
        self.assertEqual(admin_code.privileges('allowed_effects'),
                         ['let_manage'])
        self.assertEqual(AdminCode.objects.count(), 1)
        self.assertEqual(list(self.competition.organizer_codes()),
                         [self.legacy])

    def test_migrated_code_works_in_exact_form(self):
        self.migrate()
        allows = self.competition.admin_code_allows
        self.assertTrue(allows(self.legacy.value, 'admin_privileges',
                               'create_competitor_codes'))
        self.assertFalse(allows(self.legacy.value.upper(),
                                'admin_privileges',
                                'create_competitor_codes'))


class CompetitionCreateTest(TestCase):
    def test_create_form_has_no_code_format_fields(self):
        from bober_simple_competition.forms import CompetitionCreateForm
        form = CompetitionCreateForm()
        for name in ('admin_code_format', 'competitor_code_format',
                     'admin_salt', 'competitor_salt'):
            self.assertNotIn(name, form.fields)

    def test_new_competition_codes(self):
        """Code generators of new competitions have no format and salt."""
        generator = CodeGenerator.objects.create()
        self.assertIsNone(generator.format)
        self.assertEqual(generator.separator, '*')


class AttemptMergeRefusalTest(AttemptMergeTestMixin, TestCase):
    def test_attempt_without_answers_is_refused(self):
        online = self.attempt([(0, 'ok')])
        # e.g. a paper submission: score entered, no answers
        paper = self.attempt([])
        Attempt.objects.filter(id=paper.id).update(score=23)
        for target, part in ((online, paper), (paper, online)):
            with self.assertRaises(MergeError):
                target.merge([part])
        paper.refresh_from_db()
        self.assertEqual(paper.score, 23)
        self.assertFalse(Attempt.objects.filter(
            merged_into__isnull=False).exists())

    def test_confirmed_part_is_refused(self):
        first = self.attempt([(0, 'ok')])
        second = self.attempt([(1, 'ok')])
        teacher = User.objects.create_user('t', password='pw')
        AttemptConfirmation.objects.create(by=teacher.profile, attempt=second)
        with self.assertRaises(MergeError):
            first.merge([second])
        # a confirmed target is fine
        AttemptConfirmation.objects.all().delete()
        AttemptConfirmation.objects.create(by=teacher.profile, attempt=first)
        first.merge([second])
        second.refresh_from_db()
        self.assertEqual(second.merged_into, first)

    def test_view_reports_refusal(self):
        teacher = User.objects.create_user('teacher', password='pw')
        teacher.profile.created_codes.add(self.code)
        first = self.attempt([(0, 'ok')])
        paper = self.attempt([])
        self.client.login(username='teacher', password='pw')
        url = reverse('attempt_merge', kwargs={
            'competition_questionset_id': self.cqs.id})
        response = self.client.post(url, {'attempt_id': [first.id, paper.id]})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(self.client.get(url).status_code, 405)


@override_settings(CODE_AUTH_MAX_FAILURES=3)
class ThrottleClientAddressTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        cache.clear()
        self.competition, (self.cqs, _) = self.make_competition('throttle-ip')
        self.code, self.cc = self.make_code(self.cqs)
        self.url = reverse('competition_compete', kwargs={
            'slug': self.competition.slug})

    def tearDown(self):
        cache.clear()

    def post(self, code, **meta):
        return self.client.post(self.url, self.form_data(
            code, competition_questionset=self.cqs.id), **meta)

    def test_competition_compete_is_throttled(self):
        for _ in range(3):
            self.assertNotEqual(self.post('AAAAA-AAAAA').status_code, 429)
        self.assertEqual(self.post(self.cc.value).status_code, 429)

    @override_settings(CODE_AUTH_CLIENT_IP_HEADER='HTTP_X_FORWARDED_FOR')
    def test_client_address_from_proxy_header(self):
        proxy = {'REMOTE_ADDR': '10.9.9.9'}
        for _ in range(3):
            self.post('AAAAA-AAAAA', HTTP_X_FORWARDED_FOR='1.1.1.1, 2.2.2.2',
                      **proxy)
        self.assertEqual(self.post(
            self.cc.value, HTTP_X_FORWARDED_FOR='2.2.2.2', **proxy
        ).status_code, 429)
        # another client behind the same proxy is not affected
        self.assertEqual(self.post(
            self.cc.value, HTTP_X_FORWARDED_FOR='3.3.3.3', **proxy
        ).status_code, 302)



class CodeLengthTest(CompetitorCodeTestMixin, TestCase):
    def setUp(self):
        self.competition, (self.cqs, self.other_cqs) = \
            self.make_competition('length-test')

    def test_default_length(self):
        self.assertEqual(self.cqs.code_length, 10)
        code, cc = self.make_code(self.cqs)
        self.assertEqual(len(cc.value), len('XXXXX-XXXXX'))

    def test_length_per_questionset(self):
        CompetitionQuestionSet.objects.filter(id=self.cqs.id).update(
            code_length=8)
        self.cqs.refresh_from_db()
        code, cc = self.make_code(self.cqs)
        self.assertRegex(cc.value, r'^[0-9A-Z]{4}-[0-9A-Z]{4}$')
        self.assertEqual(code.value, self.cqs.slug_str() + '*' + cc.value)
        # the other group keeps the default
        other_code, other_cc = self.make_code(self.other_cqs)
        self.assertEqual(len(other_cc.value), len('XXXXX-XXXXX'))
        # typed in any form
        form = QuestionSetCompetitorForm(
            self.form_data(cc.value.replace('-', '').lower()),
            competitionquestionset=self.cqs)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['full_code'], code.value)

    def test_codes_keep_working_after_length_change(self):
        code, cc = self.make_code(self.cqs)
        CompetitionQuestionSet.objects.filter(id=self.cqs.id).update(
            code_length=6)
        self.cqs.refresh_from_db()
        self.assertEqual(
            CompetitorCode.lookup(self.cqs, cc.value.replace('-', '')), cc)
        short_code, short_cc = self.make_code(self.cqs)
        self.assertRegex(short_cc.value, r'^[0-9A-Z]{3}-[0-9A-Z]{3}$')

    def test_length_bounds(self):
        from django.core.exceptions import ValidationError
        for length in (5, 21):
            self.cqs.code_length = length
            with self.assertRaises(ValidationError):
                self.cqs.full_clean()
        self.cqs.code_length = 6
        self.cqs.full_clean()

    def test_form_has_code_length(self):
        form = CompetitionQuestionSetUpdateForm(instance=self.cqs)
        self.assertIn('code_length', form.fields)
        self.assertEqual(form.fields['code_length'].initial or
                         form.initial['code_length'], 10)
