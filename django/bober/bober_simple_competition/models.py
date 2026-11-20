from collections import OrderedDict
import random
import os
import json
import base64
import zipfile
from bs4 import BeautifulSoup
import mimetypes

from django.db.models import SlugField, CharField, TextField, IntegerField
from django.db.models import FileField, BooleanField, FloatField, Model
from django.db.models import DateField, DateTimeField, DurationField
from django.db.models import ForeignKey, ManyToManyField, OneToOneField
from django.db.models import signals, F, ExpressionWrapper, Manager
from django.db.models import BinaryField, CASCADE, SET_NULL, UniqueConstraint
from django.db import IntegrityError, transaction
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from code_based_auth.models import Code, CodeField, CodeGenerator, CodePart
from code_based_auth import random_code
from taggit.managers import TaggableManager

from . import graders


# Create your models here.
GRADER_FUNCTION_TYPES = (
    (0, 'none'),
    (1, 'javascript_gostisa'),
    (2, 'javascript_france'),
    (16, 'python'),
)


CACHE_FORMATS = (
    ('zip', 'ZIP'),
    ('raw', 'raw data'),
)


def ensure_dir_exists(fname):
    d = os.path.dirname(fname)
    try:
        os.makedirs(d)
    except Exception:
        # TODO: handle exception
        pass


GENDERS = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('na', 'Not applicable')
)


USER_ROLES = (
    ('competitor', 'Competitor'),
    ('admin', 'Administrator'),
)


COMPETITOR_PRIVILEGES = (
    ('attempt', _('Participate in the competition')),
    ('attempt_before_start', _('Attempt competition before start')),
    ('results_before_end',
     _('See results before official end of competition')),
)

COMPETITOR_PRIVILEGE_NAMES = tuple(p for p, _ in COMPETITOR_PRIVILEGES)


CODE_EFFECTS = (
    ('let_manage',
     _('Allow the creator to manage the profile of anyone using this code')),
    ('let_manage_recursive', _('Allow the creator and their managers to manage the profile of anyone using this code')),
)


ADMIN_PRIVILEGES = (
    ('create_admin_codes', _('Create administrator codes')),
    ('create_competitor_codes', _('Create comeptitor codes')),
    ('view_all_attempts', _('View all attempts for this competition')),
    ('view_all_admin_codes', _('View all administrator codes for this competition')),
    ('view_all_competitor_codes', _('View all competitor codes for this competition')),
    ('use_question_sets', _('Use question sets for new competitions')),
    ('modify_competition', _('Modify this competition')),
    ('use_questions', _('Use questions for new question sets')),
)

#   2. can create codes for competing
#       2.1 can attempt competition
#           'attempt' in components['privileges']
#       2.2 can attempt competition before official start
#           'attempt_before_start' in components['privileges']
#       2.3 can view results before official end
#           'view_before_end' in components['privileges']
#       2.4 can use questionset to create new competitions
#           'reuse_questions' in components['privileges']


FEATURE_LEVELS = [
    (0, _('Reduced functionality')),
    (1, _('Basic features only')),
    (10, _('Commonly used features')),
    (128, _('All features')),
]


class Competition(Model):
    def __str__(self):
        s = self.slug
        s += ": " + ", ".join([i.slug for i in self.questionsets.all()])
        return s

    def get_absolute_url(self):
        return reverse('competition_detail', kwargs={'slug': str(self.slug)})

    title = CharField(max_length=256, null=True, blank=True,
                      verbose_name=_("title"))
    promoted = BooleanField(default=False, verbose_name=_("promoted"))
    public = BooleanField(default=True, verbose_name=_("public competition"),
                          help_text=_("Public competitions are listed on the competiton list page")
                          )
    slug = SlugField(unique=True, verbose_name=_("slug"))
    administrator_code_generator = ForeignKey(
        CodeGenerator,
        related_name='administrator_code_competition_set',
        verbose_name=_("administrator code generator"),
        on_delete=CASCADE
    )
    competitor_code_generator = ForeignKey(
        CodeGenerator,
        related_name='competitor_code_competition_set',
        verbose_name=_("competitor code generator"),
        on_delete=CASCADE)
    questionsets = ManyToManyField(
        'QuestionSet',
        through='CompetitionQuestionSet',
        verbose_name=_("Question sets"))
    start = DateTimeField(verbose_name=_("start"))
    # duration in seconds
    duration = IntegerField(
        default=45*60,  # 60s * 45 = 1h.
        verbose_name=_("duration"),
        help_text=_("Duration of the competition in seconds"))
    end = DateTimeField(verbose_name=_("end"))
    motd = TextField(blank=True, verbose_name=_("message of the day"))

    @property
    def is_over(self):
        """
        Return true when competition is finished.
        """
        return self.end < timezone.now()

    @property
    def guests_allowed(self):
        return self.competitionquestionset_set.filter(guest_code__isnull=False).exists()

    @staticmethod
    def ongoing_competitions():
        """
        Return a list of ongoing competitions.
        Complexity: linearly dependent on the number of all competitions.
        """
        now = timezone.now()
        return Competition.objects.filter(start__lte=now, end__gte=now)

    @property
    def is_ongoing(self):
        return self.start <= timezone.now() <= self.end

    @classmethod
    def get_cached_by_slug(cls, slug):
        c = cache.get('competition_by_slug__' + slug, None)
        if c is None:
            c = cls.objects.select_related(
                'administrator_code_generator',
                'competitor_code_generator',
                'administrator_code_generator__format',
                'competitor_code_generator__format',
            ).get(slug=slug)
            print("  adding", slug, "to cache")
            cache.set('competition_by_slug__' + slug, c)
        return c

    def expand_competitor_code(self, short_code, competition_questionset):
        sep = self.competitor_code_generator.separator
        return competition_questionset.slug_str() + sep + short_code

    def split_competitor_code(self, access_code):
        sep = self.competitor_code_generator.separator
        return access_code.split(sep)

    def grade_answers(self, grader_runtime_manager=None,
                      update_graded=False, regrade=False):
        grader_runtime_manager = graders.init_runtimes(
            grader_runtime_manager)
        if grader_runtime_manager is None:
            grader_runtime_manager = graders.RuntimeManager()
            grader_runtime_manager.start_runtimes()
        if update_graded:
            self.update_graded_answers(
                regrade=regrade,
                grader_runtime_manager=grader_runtime_manager)
            if regrade:
                return
        for cq in CompetitionQuestionSet.objects.filter(competition=self):
            cq.grade_answers(grader_runtime_manager=grader_runtime_manager,
                             update_graded=False, regrade=regrade)

    def update_graded_answers(self, regrade=False,
                              grader_runtime_manager=None):
        grader_runtime_manager = graders.init_runtimes(
            grader_runtime_manager)
        for cq in CompetitionQuestionSet.objects.filter(competition=self):
            cq.update_graded_answers(
                regrade=regrade,
                grader_runtime_manager=grader_runtime_manager)

    def admin_code(self, access_code):
        """The AdminCode of this competition for access_code, or None."""
        return AdminCode.lookup(self, access_code)

    def admin_code_allows(self, access_code, kind, name):
        """True if the administrator code access_code has a privilege.

        kind is 'admin_privileges', 'competitor_privileges' or
        'allowed_effects'.
        """
        admin_code = self.admin_code(access_code)
        return admin_code is not None and admin_code.has_privilege(kind, name)

    def _privilege_choices(self, access_code, kind, choices):
        admin_code = self.admin_code(access_code)
        if admin_code is None:
            return []
        return [c for c in choices if admin_code.has_privilege(kind, c[0])]

    def admin_privilege_choices(self, access_code):
        return self._privilege_choices(
            access_code, 'admin_privileges', ADMIN_PRIVILEGES)

    def allowed_effect_choices(self, access_code):
        return self._privilege_choices(
            access_code, 'allowed_effects', CODE_EFFECTS)

    def competitor_privilege_choices(self, access_code):
        return self._privilege_choices(
            access_code, 'competitor_privileges', COMPETITOR_PRIVILEGES)

    def max_admin_code_data(self, access_code):
        return {
            'admin_privileges':
                [i[0] for i in self.admin_privilege_choices(access_code)],
            'allowed_effects':
                [i[0] for i in self.allowed_effect_choices(access_code)],
            'competitor_privileges':
                [i[0] for i in self.competitor_privilege_choices(access_code)]
            }

    def max_competitor_code_data(self, access_code):
        return {
            'competitor_privileges':
                [i[0] for i in self.competitor_privilege_choices(access_code)]
            }

    def competitor_code_create(self, access_code,
                               competition_questionset=None,
                               code_data=None):
        """Create a random competitor code; returns its Code.

        The privileges (and code effects) come from code_data, by default
        everything the administrator code access_code may hand out.
        """
        if code_data is None:
            code_data = self.max_competitor_code_data(access_code)
        if competition_questionset is None:
            slugs = code_data.get('competition_questionset')
            if isinstance(slugs, str):
                slugs = [slugs]
            competition_questionset = CompetitionQuestionSet.get_by_slug(
                slugs[0])
        if competition_questionset.competition_id != self.id:
            raise ValueError("questionset is not part of this competition")
        cc = CompetitorCode.create(
            competition_questionset,
            privileges=code_data.get('competitor_privileges', []),
            code_effects=code_data.get('code_effects', []))
        return cc.code

    def competitor_code(self, access_code):
        """The CompetitorCode of this competition for a full access code."""
        return CompetitorCode.for_competition(self, access_code)

    def master_code_create(self):
        """Create an administrator code with all privileges."""
        return AdminCode.create(self, {
            'admin_privileges': [i[0] for i in ADMIN_PRIVILEGES],
            'competitor_privileges': [i[0] for i in COMPETITOR_PRIVILEGES],
            'allowed_effects': [i[0] for i in CODE_EFFECTS],
        }).code

    def admin_code_create(self, access_code, code_data=None):
        """Create an administrator code; returns its Code.

        The privileges come from code_data, by default everything the
        administrator code access_code may hand out.
        """
        if code_data is None:
            code_data = self.max_admin_code_data(access_code)
        return AdminCode.create(
            self, code_data,
            code_effects=code_data.get('code_effects', [])).code

    def organizer_codes(self):
        """Codes of this competition that may view all administrator codes
        (used to find the organizer)."""
        return Code.objects.filter(admin_code__competition=self,
                                   admin_code__view_all_admin_codes=True)


ANSWER_BATCH_SIZE = 100000


class _AnswerQuestionIds(object):
    """Answer.question_id, computed once per (attempt, randomized id)."""
    def __init__(self):
        self.cache = {}

    def get(self, answer):
        key = (answer.attempt_id, answer.randomized_question_id)
        if key not in self.cache:
            try:
                self.cache[key] = answer.question_id
            except Exception:
                # unknown question; keep the old per-attempt behaviour
                self.cache[key] = key
        return self.cache[key]


def _create_graded(answer, regrade, grader_runtime_manager,
                   attempt_id=None):
    """Grade an answer for attempt_id (default: the answer's attempt).

    attempt_id differs from answer.attempt_id for answers of attempts that
    were merged into another attempt; the answer is still graded with the
    random seed of its own attempt.
    """
    if attempt_id is None:
        attempt_id = answer.attempt_id
    try:
        a = answer
        if regrade:
            # print a
            g_a = GradedAnswer(
                attempt_id=attempt_id, question_id=a.question_id,
                answer=a
            )
            q = Question.objects.get(id=g_a.question_id)
            grader = grader_runtime_manager.get_grader(
                q.verification_function, q.verification_function_type)
            g_a.score = grader(a.value, a.attempt.random_seed, q)
            return g_a
        else:
            g_a, created = GradedAnswer.objects.get_or_create(
                attempt_id=attempt_id, question_id=a.question_id,
                defaults={'answer': a, 'score': None})
            if not created and g_a.answer != a:
                g_a.answer = a
                g_a.score = None
                g_a.save()
    except Exception as e:
        print(e)
    return None


class CompetitionQuestionSet(Model):
    def __str__(self):
        return u"{}: {}".format(self.competition.slug, self.name)

    name = CharField(max_length=256, null=True, blank=True,
                     verbose_name=("Name"))
    questionset = ForeignKey('QuestionSet', verbose_name=_("Questionset"),
                             on_delete=CASCADE)
    competition = ForeignKey('Competition', on_delete=CASCADE)
    guest_code = ForeignKey(Code, null=True, blank=True, on_delete=CASCADE)

    def slug_str(self):
        return str(self.id) + '-' + self.questionset.slug

    @classmethod
    def get_by_slug(cls, slug):
        return cls.objects.get(id=slug[:slug.find('-')])

    def grade_answers(self, grader_runtime_manager=None,
                      update_graded=False, regrade=False):
        grader_runtime_manager = graders.init_runtimes(
            grader_runtime_manager)
        if update_graded:
            self.update_graded_answers(
                regrade=regrade,
                grader_runtime_manager=grader_runtime_manager)
            if regrade:
                return
        graded_answers = GradedAnswer.objects.filter(
            attempt__competitionquestionset=self).distinct()
        if not regrade:
            graded_answers = graded_answers.filter(score=None)
        graded_answers = graded_answers.select_related(
            'question', 'answer__attempt')
        for g_a in graded_answers:
            q = g_a.question
            grader = grader_runtime_manager.get_grader(
                q.verification_function, q.verification_function_type)
            # the seed of the attempt the answer was given in
            g_a.score = grader(g_a.answer.value,
                               g_a.answer.attempt.random_seed, q)
            g_a.save()

    def update_graded_answers(self, check_timestamp=False,
                              regrade=False, grader_runtime_manager=None):
        grader_runtime_manager = graders.init_runtimes(
            grader_runtime_manager)
        answers = Answer.objects.filter(
            attempt__competitionquestionset=self).order_by(
                '-id').select_related('attempt')
        if check_timestamp:
            answers.select_related('attempt__finish')
        if regrade:
            answers.select_related('attempt__random_seed')
            GradedAnswer.objects.filter(
                attempt__competitionquestionset=self).delete()
        graded_list = []
        grades_set = set()
        question_ids = _AnswerQuestionIds()
        for a in answers:
            # answers of merged attempts are graded for the attempt they
            # were merged into
            graded_attempt_id = a.attempt.merged_into_id or a.attempt_id
            if not check_timestamp or a.timestamp < a.attempt.finish:
                key = (graded_attempt_id, question_ids.get(a))
                if key in grades_set:
                    continue
                g_a = _create_graded(a, regrade, grader_runtime_manager,
                                     attempt_id=graded_attempt_id)
                if g_a:
                    graded_list.append(g_a)
                grades_set.add(key)
            if len(graded_list) > ANSWER_BATCH_SIZE:
                GradedAnswer.objects.bulk_create(graded_list)
                graded_list = []
                grades_set.clear()
        GradedAnswer.objects.bulk_create(graded_list)


class CompetitorCode(Model):
    """A competitor access code.

    The value is a random string (see code_based_auth.random_code) that is
    only valid for one CompetitionQuestionSet; the same value may exist in
    other questionsets. A code is checked by looking up the pair
    (competition questionset, value); what it allows is stored in the flags
    below, not in the value.

    The full access code (stored in Code.value, in the session and in
    Attempt.access_code) is the questionset slug, the separator of the
    competitor code format and the value, as for older codes.
    """
    def __str__(self):
        return self.code.value

    code = OneToOneField(Code, related_name='competitor_code',
                         on_delete=CASCADE)
    competition_questionset = ForeignKey(
        'CompetitionQuestionSet', related_name='competitor_codes',
        on_delete=CASCADE)
    value = CharField(max_length=256)
    attempt = BooleanField(default=False)
    attempt_before_start = BooleanField(default=False)
    results_before_end = BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['competition_questionset', 'value'],
                name='unique_competitor_code_value_per_cqs'),
        ]

    MAX_CREATE_TRIES = 10

    def has_privilege(self, privilege):
        return privilege in COMPETITOR_PRIVILEGE_NAMES \
            and getattr(self, privilege)

    @property
    def privileges(self):
        return [p for p in COMPETITOR_PRIVILEGE_NAMES if getattr(self, p)]

    @staticmethod
    def _prefix(competition_questionset):
        competition = competition_questionset.competition
        separator = competition.competitor_code_generator.separator
        return competition_questionset.slug_str() + separator

    @classmethod
    def create(cls, competition_questionset, privileges=(),
               code_effects=()):
        """Store a new random code; retry when the value is already used."""
        generator = \
            competition_questionset.competition.competitor_code_generator
        prefix = cls._prefix(competition_questionset)
        flags = dict((p, p in privileges) for p in COMPETITOR_PRIVILEGE_NAMES)
        for _try in range(cls.MAX_CREATE_TRIES):
            value = random_code.generate()
            try:
                with transaction.atomic():
                    code = Code.objects.create(value=prefix + value)
                    cc = cls.objects.create(
                        code=code,
                        competition_questionset=competition_questionset,
                        value=value, **flags)
            except IntegrityError:
                if cls.objects.filter(
                        competition_questionset=competition_questionset,
                        value=value).exists():
                    continue  # value already used: try another one
                raise
            for i, effect in enumerate(code_effects):
                CodePart.objects.create(code=code, ordering=i,
                                        name='code_effects', value=effect)
            generator.codes.add(code)
            return cc
        raise RuntimeError("could not create a unique competitor code")

    @classmethod
    def lookup(cls, competition_questionset, typed):
        """Find the code a competitor typed for a questionset, or None."""
        values = random_code.lookup_values(typed)
        if not values:
            return None
        found = dict((cc.value, cc) for cc in cls.objects.filter(
            competition_questionset=competition_questionset,
            value__in=values).select_related('code'))
        for v in values:
            if v in found:
                return found[v]
        return None

    @classmethod
    def from_access_code(cls, competition_questionset, access_code):
        """Find the code for a full access code (questionset slug + value).

        Returns None if the access code belongs to another questionset.
        """
        if not access_code:
            return None
        prefix = cls._prefix(competition_questionset)
        if not access_code.startswith(prefix):
            return None
        return cls.lookup(competition_questionset, access_code[len(prefix):])

    @classmethod
    def for_competition(cls, competition, access_code):
        """Find the code for a full access code of any questionset of
        the competition."""
        try:
            cqs_id = int(access_code[:access_code.index('-')])
        except (AttributeError, TypeError, ValueError):
            return None
        cqs = competition.competitionquestionset_set.filter(
            id=cqs_id).first()
        if cqs is None:
            return None
        return cls.from_access_code(cqs, access_code)


# kind of privilege -> {privilege name: AdminCode field}
ADMIN_CODE_FIELDS = {
    'admin_privileges': dict((p, p) for p, _ in ADMIN_PRIVILEGES),
    'competitor_privileges': dict(
        (p, 'competitor_' + p) for p, _ in COMPETITOR_PRIVILEGES),
    'allowed_effects': dict((e, 'allow_' + e) for e, _ in CODE_EFFECTS),
}


class AdminCode(Model):
    """An administrator access code of a competition.

    Like CompetitorCode: the value is random (code_based_auth.random_code),
    the privileges are stored in the fields below and a code is checked by
    looking up (competition, value). Administrator codes are typed on a page
    that does not know the competition, so the full access code (Code.value,
    session) is the value itself, without a prefix.
    """
    def __str__(self):
        return self.code.value

    code = OneToOneField(Code, related_name='admin_code', on_delete=CASCADE)
    competition = ForeignKey('Competition', related_name='admin_codes',
                             on_delete=CASCADE)
    value = CharField(max_length=256)
    # admin_privileges
    create_admin_codes = BooleanField(default=False)
    create_competitor_codes = BooleanField(default=False)
    view_all_attempts = BooleanField(default=False)
    view_all_admin_codes = BooleanField(default=False)
    view_all_competitor_codes = BooleanField(default=False)
    use_question_sets = BooleanField(default=False)
    modify_competition = BooleanField(default=False)
    use_questions = BooleanField(default=False)
    # competitor_privileges (what competitor codes created with it may get)
    competitor_attempt = BooleanField(default=False)
    competitor_attempt_before_start = BooleanField(default=False)
    competitor_results_before_end = BooleanField(default=False)
    # allowed_effects
    allow_let_manage = BooleanField(default=False)
    allow_let_manage_recursive = BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['competition', 'value'],
                name='unique_admin_code_value_per_competition'),
        ]

    MAX_CREATE_TRIES = 10

    def has_privilege(self, kind, name):
        field = ADMIN_CODE_FIELDS.get(kind, {}).get(name)
        return field is not None and getattr(self, field)

    def privileges(self, kind):
        return [name for name, field in ADMIN_CODE_FIELDS[kind].items()
                if getattr(self, field)]

    @classmethod
    def flags(cls, privileges):
        """Field values for a dict {kind: [privilege names]}."""
        flags = {}
        for kind, fields in ADMIN_CODE_FIELDS.items():
            given = privileges.get(kind, ())
            for name, field in fields.items():
                flags[field] = name in given
        return flags

    @classmethod
    def create(cls, competition, privileges, code_effects=()):
        """Store a new random code; retry when the value is already used."""
        generator = competition.administrator_code_generator
        flags = cls.flags(privileges)
        for _try in range(cls.MAX_CREATE_TRIES):
            value = random_code.generate()
            try:
                with transaction.atomic():
                    code = Code.objects.create(value=value)
                    admin_code = cls.objects.create(
                        code=code, competition=competition, value=value,
                        **flags)
            except IntegrityError:
                if cls.objects.filter(competition=competition,
                                      value=value).exists():
                    continue  # value already used: try another one
                raise
            for i, effect in enumerate(code_effects):
                CodePart.objects.create(code=code, ordering=i,
                                        name='code_effects', value=effect)
            generator.codes.add(code)
            return admin_code
        raise RuntimeError("could not create a unique administrator code")

    @classmethod
    def lookup(cls, competition, typed):
        """Find an administrator code of competition, or None."""
        values = random_code.lookup_values(typed)
        if not values:
            return None
        found = dict((ac.value, ac) for ac in cls.objects.filter(
            competition=competition, value__in=values).select_related('code'))
        for v in values:
            if v in found:
                return found[v]
        return None


class CodeEffect(Model):
    code = ForeignKey(Code, on_delete=CASCADE)
    effect = CharField(max_length=64, choices=CODE_EFFECTS)

    def apply(self, users=None):
        def let_manage(profile):
            for owner in self.code.owner_set:
                owner.managed_profiles.add(profile)

        def let_manage_recursive(profile):
            competitions = Competition.objects.filter(
                competitor_code_generator=self.generator).unique()
            for owner in self.code.owner_set:
                owner.managed_profiles.add(profile)
                for competition in competitions:
                    # TODO: superiors???
                    for superior in __superiors(
                            owner,
                            competition.administrator_code_generator):
                        superior.managed_profiles.add(profile)
        effects = {
            'let_manage': let_manage,
            'let_manage_recursive': let_manage_recursive
        }
        if users is None:
            users = self.code.user_set.all()
        # actually apply the effects
        for user in users:
            effects[self.effect](user)


class QuestionSet(Model):
    def __str__(self):
        return u"{}".format(self.name)

    def get_absolute_url(self):
        return reverse('questionset_detail', kwargs={'pk': str(self.id)})

    slug = SlugField(unique=True, verbose_name=_("Slug"))
    name = CharField(max_length=255, verbose_name=_("Name"))
    questions = ManyToManyField('Question', blank=True,
                                verbose_name=_("Questions"))
    resource_caches = ManyToManyField('ResourceCache', blank=True)

    def question_mapping(self, random_seed):
        q = self.questions.order_by('identifier').values_list('identifier')
        d = dict()
        r = random.Random(random_seed)
        c = r.sample(range(2**24), len(q))
        for n, i in enumerate(q):
            d[i[0]] = c[n]
        return d

    def ordered_question_ids(self):
        cache_id = 'questionset_question_ids_' + str(self.id)
        q_ids = cache.get(cache_id, None)
        if q_ids is None:
            q_ids = self.questions.order_by('id').values_list(
                'id', flat=True)
            cache.set(cache_id, q_ids)
        return q_ids

    def cache_dir(self):
        return str(self.id) + "-" + self.slug

    def reverse_question_mapping(self, random_seed):
        return {v: k for k, v in self.question_mapping(random_seed).items()}

    def rebuild_caches(self, embed_images=True):
        html_resources = {}
        self.resource_caches.all().delete()
        html_cache = ResourceCache(format='zip')
        html_cache.file.name = os.path.join("caches", self.cache_dir(),
                                            "html_cache.zip")
        html_cache.save()
        ensure_dir_exists(html_cache.file.path)
        embeded_resource_ids = []
        html_resource_zip = zipfile.ZipFile(html_cache.file.path, 'w')
        for q in self.questions.all():
            for r in q.resource_set.filter(
                    resource_type="html",
                    part_of_solution=False):
                html_resources[q.identifier + '/' + r.relative_url] = r
                html_resource_zip.writestr(
                    q.identifier + '/' + 'Manifest.json',
                    json.dumps(q.manifest(safe=True)))
        for url, r in html_resources.items():
            if embed_images:
                index_soup = BeautifulSoup(r.as_bytes(), "lxml")
                imgs = index_soup.find_all('img')
                objs = index_soup.find_all('object')
                scripts = index_soup.find_all('script')
                for items, item_type, url_property in [
                        (imgs, 'image', 'src'),
                        (objs, 'image', 'data'),
                        (scripts, 'javascript', 'src')]:
                    for i in items:
                        url_str = i.get(url_property, None)
                        if url_str is not None:
                            try:
                                data_res = r.question.resource_set.get(relative_url=url_str)
                                i[url_property] = ("data:" + data_res.mimetype + ";base64," +
                                                   data_res.as_base64().decode('utf-8'))
                                embeded_resource_ids.append(data_res.id)
                            except Exception as e:
                                # TODO: handle exception, not print it!
                                if not url_str.startswith('/static/'):
                                    print("error embedding", url, url_str, e)
                embeded_resource_ids.append(r.id)
                index_str = bytes(index_soup.prettify().encode('utf-8'))
            else:
                index_str = r.as_bytes()
            html_resource_zip.writestr(url, index_str)
            html_cache.resources.add(r)
        html_resource_zip.close()
        self.resource_caches.add(html_cache)
        for q in self.questions.all():
            for r in q.resource_set.exclude(part_of_solution=True).exclude(
                    id__in=embeded_resource_ids):
                print("must create cache for ", r.id, r.question.identifier,
                      r.file.name)


def _qs_rebuild_caches(sender, instance=None, **kwargs):
    if instance is not None:
        instance.rebuild_caches()
        signals.m2m_changed.connect(_qs_rebuild_caches, sender=QuestionSet)


class ResourceCache(Model):
    def __str__(self):
        return u"{}: {}".format(self.format, self.file)
    file = FileField(upload_to='caches')
    format = CharField(max_length=16, choices=CACHE_FORMATS)
    resources = ManyToManyField('Resource')


class Resource(Model):
    def __str__(self):
        return u"{}: {}".format(self.relative_url, self.file)
    question = ForeignKey('Question', on_delete=CASCADE)
    relative_url = CharField(max_length=255)
    file = FileField(null=True, upload_to='resources')
    resource_type = CharField(max_length=255)
    mimetype = CharField(max_length=255)
    data = BinaryField(null=True)
    part_of_solution = BooleanField(default=False)

    def url(self):
        return self.file.url

    def as_bytes(self):
        s = bytes()
        if self.file:
            self.file.open()
            s = self.file.read()
            self.file.close()
        elif self.data is not None:
            fname = os.path.join('resources', self.question.identifier,
                                 self.relative_url)
            self.file.name = fname
            ensure_dir_exists(self.file.path)
            with open(self.file.path, 'wb') as f:
                f.write(self.data)
            s = self.data
        return s

    def as_base64(self):
        return base64.b64encode(self.as_bytes())


def _resource_list(soup):
    resource_set = set()
    imgs = soup.find_all('img')
    objs = soup.find_all('object')
    scripts = soup.find_all('script')
    for items, item_type, url_property in [
            (imgs, 'image', 'src'),
            (objs, 'image', 'data'),
            (scripts, 'javascript', 'src')]:
        for i in items:
            url = i.get(url_property, None)
            if url is not None:
                resource_set.add((item_type, url))
    return [
        {'type': item_type, 'url': url} for item_type, url in resource_set
    ]


def _question_from_dirlike(
        cls, identifier='-1',
        language=None,
        regenerate_modules=True,
        regenerate_manifest=True,
        remove_correct_answer_class=True,
        my_open=None, my_path=None, my_close=None):
    question = None
    if language is None:
        language = settings.LANGUAGE_CODE.split('-')[0]
    try:
        f = my_open(my_path('Manifest.json'))
        manifest = json.load(f)
    except Exception as e:
        manifest = {
            'id': identifier,
            'language': language}
        print(" no manifest? ", e)
        regenerate_manifest = True
    try:
        my_close(f)
    except Exception:
        # TODO: handle exception
        pass
    identifier = manifest['id']
    language = manifest['language']
    # get properties from database into question_dict
    try:
        question = cls.objects.filter(identifier=identifier)
        q1 = question.filter(language=language)
        if len(q1) == 1:
            question = q1
        elif len(question) < 1:
            raise ObjectDoesNotExist
        if len(question) > 1:
            raise MultipleObjectsReturned
        question_dict = question.values()[0]
        question_dict['id'] = question_dict.pop('identifier')
        question = question[0]
        resource_list = []
        for resource in question.resource_set.all():
            resource_list.append({'url': resource.url,
                                  'type': resource.resource_type})
        question_dict['task'] = resource_list
    except ObjectDoesNotExist:
        question = None
        regenerate_modules = True
    # read index
    f = my_open(my_path('index.html'))
    index_str = f.read()
    my_close(f)
    # get properties from index
    index_dict = {}
    index_soup = BeautifulSoup(index_str, "lxml")
    try:
        index_dict['title'] = str(index_soup.title.contents[0]).strip()
    except Exception:
        # TODO: handle exception
        pass
    try:
        index_dict['version'] = index_soup.find(
            'meta', {'name': 'revision'}).attrs['content']
    except Exception:
        # TODO: handle exception
        pass
    try:
        index_dict['country'] = index_soup.find(
            'meta', {'name': 'geo.country'}).attrs['content'].upper()
    except Exception:
        # TODO: handle exception
        pass

    # all correct answers should be marked by the class "answer_accepted"
    answers = index_soup.select('input[name="answer"]')
    accepted_answers = []
    for a in answers:
        class_list = []
        for c in a.get("class", []):
            if c == 'answer_accepted':
                accepted_answers.append(a['value'])
            else:
                class_list.append(c)
        if len(class_list):
            a['class'] = class_list
        else:
            del a['class']
    if len(accepted_answers) > 0:
        index_dict['acceptedAnswers'] = accepted_answers
    # find all bitmaps and .svgs
    resource_list = _resource_list(index_soup)
    index_dict['task'] = [
        {'type': "html", "url": "index.html"}] + resource_list
    if regenerate_manifest:
        manifest.update(index_dict)
    if regenerate_modules:
        manifest['task'] = index_dict['task']
    default_manifest_values = {
        'country': 'SI',
        'version': '0.1',
        'authors': ''
    }
    for k, v in default_manifest_values.items():
        if k not in manifest:
            manifest[k] = v
    if question is None:
        question = cls(
            country=manifest['country'],
            slug=slugify(manifest['title'])[:30] + '-' + manifest['id'],
            identifier=manifest['id'], title=manifest['title'],
            version=manifest['version'], authors=manifest['authors'],
            verification_function=",".join(manifest['acceptedAnswers']))
        question.save()
    else:
        question.country = manifest['country']
        question.slug = slugify(manifest['title'])[:30] + '-' + manifest['id']
        question.title = manifest['title']
        question.version = manifest['version']
        question.authors = manifest['authors']
        question.verification_function = ",".join(manifest['acceptedAnswers'])
        question.save()
    resource_list = manifest['task']
    modules_list = []
    # remove existing resources
    question.resource_set.all().delete()
    for i in resource_list:
        try:
            fname = my_path(i['url'])
            if fname.startswith('/static/'):
                continue
            f = my_open(fname, 'rb')
            data = f.read()
            my_close(f)
            r = Resource(
                question=question,
                relative_url=i['url'],
                file=None,
                mimetype=mimetypes.guess_type(i['url'])[0],
                resource_type=i['type'],
                data=data)
            r.save()
        except Exception as e:
            print(i, ": ", e)
            modules_list.append(i)
    return question


class Question(Model):
    def __str__(self):
        return self.title
    country = CharField(max_length=5)
    slug = SlugField()
    identifier = CharField(max_length=64, unique=True)
    title = TextField()
    tags = TaggableManager(blank=True)
    version = CharField(max_length=255, default='0')
    verification_function_type = IntegerField(
        choices=GRADER_FUNCTION_TYPES, default=0)
    verification_function = TextField(default="", blank=True)
    license = TextField(default="Creative commons CC-By")
    language = CharField(max_length=7, choices=settings.LANGUAGES)
    authors = TextField(default="Various")
    min_score = FloatField(default=-1)
    none_score = FloatField(default=0)
    max_score = FloatField(default=1)

    def index(self):
        for u in ['index.html', 'index.htm']:
            try:
                return self.resource_set.get(relative_url=u)
            except Exception:
                # TODO: handle exception
                pass
        return None

    def solution(self):
        for u in ['solution.html']:
            try:
                return self.resource_set.get(relative_url=u)
            except Exception:
                # TODO: handle exception
                pass
        return None

    def index_str(self, embed_resources=True):
        raw_index = self.index().as_bytes()
        return raw_index

    def manifest(self, safe=True):
        manifest = dict()
        manifest['id'] = self.identifier
        manifest['language'] = self.language
        manifest['country'] = self.country
        manifest['title'] = self.title
        manifest['version'] = self.version
        manifest['authors'] = self.authors
        manifest['license'] = self.license
        manifest['task'] = []
        manifest['solution'] = []
        manifest['task_modules'] = []
        manifest['solution_modules'] = []
        manifest['grader_modules'] = []
        for i in self.resource_set.filter(part_of_solution=False):
            manifest['task'].append({"type": i.resource_type,
                                     'url': i.relative_url})
        if not safe:
            for i in self.resource_set.filter(part_of_solution=True):
                manifest['solution'].append({"type": i.resource_type,
                                             'url': i.relative_url})
            manifest['acceptedAnswers'] = [int(i) for i in
                                           self.accepted_answers.split(',')]
        return manifest

    @classmethod
    def from_zip(cls, f, identifier='-1',
                 language=None, regenerate_modules=True,
                 regenerate_manifest=True,
                 remove_correct_answer_class=True):
        z = zipfile.ZipFile(f)
        # TODO: kwargs!?
        kwargs['my_open'] = z.open
        kwargs['my_path'] = lambda *x: '/'.join(x)
        kwargs['my_close'] = lambda x: None
        retval = __question_from_dirlike(cls, *args, **kwargs)
        z.close()
        return retval

    @classmethod
    def from_dir(cls, dirname, *args, **kwargs):
        kwargs['my_open'] = open
        kwargs['my_path'] = lambda *x: os.path.join(dirname, *x)
        kwargs['my_close'] = lambda x: x.close()
        return _question_from_dirlike(cls, *args, **kwargs)


class Answer(Model):
    def __str__(self):
        return "{} ({}): {}".format(
            str(self.attempt.reverse_question_mapping().get(
                self.randomized_question_id, "??")),
            str(self.randomized_question_id),
            str(self.value))

    attempt = ForeignKey('Attempt', on_delete=CASCADE)
    randomized_question_id = IntegerField()
    timestamp = DateTimeField(auto_now_add=True)
    value = TextField(blank=True, null=True)
    score = FloatField(null=True)
    remote_addr = CharField(max_length=128, blank=True, null=True)

    @property
    def question(self):
        return Question.objects.get(identifier=self.question_identifier)

    @property
    def question_id(self):
        return Question.objects.filter(
                identifier=self.question_identifier
            ).values_list('id', flat=True)[0]

    @property
    def question_identifier(self):
        return self.attempt.reverse_question_id(
            self.randomized_question_id)


class AttemptInvalidation(Model):
    by = ForeignKey('Profile', on_delete=CASCADE)
    reason = TextField(blank=True)


class AttemptConfirmation(Model):
    def __str__(self):
        return u"{}: {}".format(self.by, self.attempt)
    by = ForeignKey('Profile', on_delete=CASCADE)
    attempt = ForeignKey('Attempt', on_delete=CASCADE)


class Competitor(Model):
    def __str__(self):
        return u"{} {} ({})".format(self.first_name, self.last_name,
                                    self.profile or '?')
    profile = ForeignKey('Profile', null=True, blank=True, on_delete=CASCADE)
    date_of_birth = DateField(verbose_name=_("Date of birth"), blank=True, null=True)
    first_name = CharField(max_length=128, verbose_name=_("First Name"))
    last_name = CharField(max_length=128, verbose_name=_("Last Name"))


class GradedAnswer(Model):
    attempt = ForeignKey('Attempt', on_delete=CASCADE)
    question = ForeignKey('Question', on_delete=CASCADE)
    answer = ForeignKey('Answer', on_delete=CASCADE)
    score = FloatField(null=True)


class AttemptManager(Manager):
    def get_queryset(self):
        duration = ExpressionWrapper(F('finish') - F('start'),
                                     output_field=DurationField())
        qs = super(AttemptManager, self).get_queryset().annotate(
            duration=duration)
        return qs


class MergeError(ValueError):
    """Attempts can not be merged; the message is shown to the teacher."""


class Attempt(Model):
    def __str__(self):
        return u"({}) {}, {} - {}: {} ({} - {})".format(
            self.id, self.competitor,
            self.competition.slug,
            self.questionset.name,
            self.access_code,
            self.start, self.finish)

    access_code = CodeField()
    competitionquestionset = ForeignKey('CompetitionQuestionSet', on_delete=CASCADE)
    competitor = ForeignKey('Competitor', null=True, blank=True, on_delete=CASCADE)
    invalidated_by = ForeignKey('AttemptInvalidation', null=True, blank=True, on_delete=CASCADE)
    confirmed_by = ManyToManyField('Profile', through='AttemptConfirmation',
                                   blank=True)
    random_seed = IntegerField()
    start = DateTimeField(auto_now_add=True)
    finish = DateTimeField(null=True, blank=True)
    score = FloatField(null=True, blank=True)
    # A teacher can merge attempts of one competitor (e.g. after a broken
    # connection) into the first of them. Merged attempts keep their own
    # answers; their answers count for merged_into. Splitting sets
    # merged_into back to None.
    merged_into = ForeignKey('self', null=True, blank=True,
                             related_name='merged_attempts',
                             on_delete=SET_NULL)
    merged_by = ForeignKey('Profile', null=True, blank=True,
                           related_name='+', on_delete=SET_NULL)
    objects = AttemptManager()

    @property
    def competition(self):
        return self.competitionquestionset.competition

    @property
    def questionset(self):
        return self.competitionquestionset.questionset

    @property
    def valid(self):
        return self.invalidated_by is None

    def reverse_question_mapping(self):
        return self.questionset.reverse_question_mapping(self.random_seed)

    def reverse_question_id(self, randomized_question_id):
        return self.reverse_question_mapping()[randomized_question_id]

    def question_mapping(self):
        return self.questionset.question_mapping(self.random_seed)

    def grade_answers(self, grader_runtime_manager=None,
                      update_graded=False, regrade=False):
        # print "grading...", self
        grader_runtime_manager = graders.init_runtimes(
            grader_runtime_manager)
        if update_graded:
            self.update_graded_answers(
                grader_runtime_manager=grader_runtime_manager,
                regrade=regrade)
            if regrade:
                return
        graded_answers = self.gradedanswer_set.all()
        if not regrade:
            graded_answers = graded_answers.filter(score=None)
        graded_answers = graded_answers.select_related(
            'question', 'answer__attempt')
        for g_a in graded_answers:
            # print "    regrading", g_a.answer
            q = g_a.question
            grader = grader_runtime_manager.get_grader(
                q.verification_function, q.verification_function_type)
            # the seed of the attempt the answer was given in (merged
            # attempts have their own seeds)
            g_a.score = grader(g_a.answer.value,
                               g_a.answer.attempt.random_seed, q)
            g_a.save()
            # a.answer.score = a.score
            # a.answer.save()

    def update_graded_answers(self, check_timestamp=False,
                              grader_runtime_manager=None,
                              regrade=False):
        answered_questions = set()
        graded_list = []
        if regrade:
            GradedAnswer.objects.filter(attempt=self).delete()
        # answers = self.answer_set.order_by("-timestamp", "-id")
        # the latest answer to each question over this attempt and the
        # attempts merged into it
        answers = Answer.objects.filter(
            attempt_id__in=self.merged_attempt_ids()).order_by(
                "-id").select_related('attempt')
        if check_timestamp:
            answers = answers.filter(timestamp__lte=F('attempt__finish'))
        n_questions = self.questionset.questions.count()
        n_found = 0
        question_ids = _AnswerQuestionIds()
        for a in answers.all():
            # print "a:", a
            question_id = question_ids.get(a)
            if question_id not in answered_questions:
                g_a = _create_graded(a, regrade, grader_runtime_manager,
                                     attempt_id=self.id)
                answered_questions.add(question_id)
                if g_a:
                    graded_list.append(g_a)
                n_found += 1
                if n_found >= n_questions:
                    break
        GradedAnswer.objects.bulk_create(graded_list)

    def latest_answers(self):
        # get only the latest answers
        return self.gradedanswer_set.all()

    @property
    def is_merged(self):
        """True if this attempt was merged into another attempt."""
        return self.merged_into_id is not None

    def merged_attempt_ids(self):
        """Ids of this attempt and of the attempts merged into it."""
        return [self.id] + list(Attempt.objects.filter(
            merged_into=self).values_list('id', flat=True))

    def regrade(self, grader_runtime_manager=None):
        """Grade again from the answers; update the score if it was set."""
        grader_runtime_manager = graders.init_runtimes(
            grader_runtime_manager)
        self.update_graded_answers(
            regrade=True, grader_runtime_manager=grader_runtime_manager)
        if self.score is not None:
            self.score = sum(max(0, a.score or 0)
                             for a in self.latest_answers())
            self.save(update_fields=['score'])

    def merge(self, attempts, by=None):
        """Merge attempts into this one.

        The answers of all attempts count for this attempt (the latest
        answer to each question). Nothing is deleted: the merged attempts
        keep their answers and can be split off again with split().
        Attempts merged into one of the given attempts are moved here.
        """
        attempts = [a for a in attempts if a.id != self.id]
        if self.is_merged:
            raise MergeError(_("Can not merge into a merged attempt."))
        for a in attempts:
            if a.competitionquestionset_id != self.competitionquestionset_id:
                raise MergeError(
                    _("Only attempts of the same group can be merged."))
            if a.is_merged:
                raise MergeError(_("An attempt is already merged."))
            # Confirmations and awards of merged attempts would still count
            # (or be printed) next to the ones of this attempt.
            if a.confirmed_by.exists() or (
                    hasattr(a, 'attemptaward_set')  # bober_si awards
                    and a.attemptaward_set.filter(revoked_by=None).exists()):
                raise MergeError(_(
                    "Confirmed attempts and attempts with awards can only "
                    "be merged into another attempt after they are "
                    "unconfirmed and their awards revoked."))
        # Scores of attempts without answers (e.g. paper submissions) were
        # entered, not graded, and would be lost by regrading.
        with_answers = set(Answer.objects.filter(
            attempt_id__in=[self.id] + [a.id for a in attempts]).values_list(
                'attempt_id', flat=True))
        if any(a.id not in with_answers for a in [self] + attempts):
            raise MergeError(
                _("Only attempts with answers given online can be merged."))
        ids = [a.id for a in attempts]
        with transaction.atomic():
            Attempt.objects.filter(merged_into_id__in=ids).update(
                merged_into=self)
            Attempt.objects.filter(id__in=ids).update(
                merged_into=self, merged_by=by)
            self.regrade()

    def split(self):
        """Undo merge(): every merged attempt is on its own again."""
        parts = list(Attempt.objects.filter(merged_into=self))
        with transaction.atomic():
            Attempt.objects.filter(merged_into=self).update(
                merged_into=None, merged_by=None)
            manager = graders.init_runtimes(None)
            self.regrade(manager)
            for a in parts:
                a.merged_into = None
                a.regrade(manager)
        return parts

    def graded_answers_by_question_id(self):
        # return self.graded_answers.order_by('gradedanswer__question_id')
        answered_questions = OrderedDict()
        # print "loading."
        graded_answers_dict = dict((i.question_id, i)
                                   for i in self.gradedanswer_set.all())
        for q_id in self.questionset.ordered_question_ids():
            answered_questions[q_id] = graded_answers_dict.get(q_id, None)
        return answered_questions

    def latest_answers_sum(self):
        return float(sum([a.score for a in self.gradedanswer_set.all()
                          if a.score is not None]))


class Profile(Model):
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': str(self.pk)})

    user = OneToOneField(User, on_delete=CASCADE)
    feature_level = IntegerField(choices=FEATURE_LEVELS, default=1)
    date_of_birth = DateField(
        null=True, blank=True,
        verbose_name=_('Date of birth'))
    gender = CharField(choices=GENDERS, max_length=16, blank=True)
    managed_profiles = ManyToManyField('Profile', related_name='managers',
                                       blank=True)
    created_codes = ManyToManyField(Code, blank=True,
                                    related_name='creator_set')
    received_codes = ManyToManyField(Code, blank=True,
                                     related_name='recipient_set')
    used_codes = ManyToManyField(Code, blank=True, related_name='user_set')
    question_sets = ManyToManyField(QuestionSet, blank=True)
    created_question_sets = ManyToManyField(QuestionSet, blank=True,
                                            related_name='creator_set')
    questions = ManyToManyField(Question, blank=True)
    merged_with = ForeignKey('Profile', null=True, blank=True,
                             related_name='former_profile_set', on_delete=CASCADE)
    update_used_codes_timestamp = DateTimeField(null=True, blank=True)
    update_managers_timestamp = DateTimeField(null=True, blank=True)
    vcard = TextField(blank=True)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

    @property
    def username(self):
        return self.user.username

    def __superiors(self, codegen, known):
        for c in self.received_codes.filter(
                format=codegen.format,
                salt=codegen.salt):
            for o in c.owner_set.all():
                if o not in known:
                    s1 = Profile.__superiors(o, codegen, known)
                    known = s1.union(known)
                    known.add(o)
        return known

    def manages_self(self):
        return self.managed_profiles.filter(id=self.id).exists()

    def managed_others(self):
        return self.managed_profiles.exclude(id=self.id)

    def update_used_codes(self):
        if self.update_used_codes_timestamp is None:
            attempts = self.attempt_set.all()
        else:
            attempts = self.attempt_set.filter(
                start__gte=self.update_used_codes_timestamp)
            self.update_used_codes_timestamp = timezone.now()
        for a in attempts:
            try:
                codegen = a.competitionquestionset.competition.competitor_code_generator
                codes = codegen.codes.filter(value=a.access_code)
                for c in codes:
                    self.used_codes.add(c)
            except Exception:
                # TODO: handle exception
                pass

    def apply_code_effects(self, codes=None):
        if codes is None:
            codes = self.used_codes
        for c in codes:
            for effect in c.code_effect_set:
                effect.apply(users=[self])

    def update_managers(self, codes=None):
        for c in codes:
            if c.has_part('code_effects', 'let_manage'):
                for u in c.owner_set:
                    u.managed_profiles.add(self)
            if c.has_part('code_effects', 'let_manage_recursive'):
                competitions = Competition.objects.filter(
                    competitor_code_generator__salt=c.salt,
                    competitor_code_generator__format=c.format).unique()
                superiors = set()
                for u in c.owner_set:
                    superiors.add(u)
                    for competition in competitions:
                        superiors = u.__superiors(
                                competition.administrator_code_generator,
                                superiors)
                for superior in superiors:
                    superior.managed_profiles.add(self)

    def update_managed_profiles(self, codes=None):
        if codes is None:
            codes = Code.objects.filter(owner_set=self).unique()
        for c in codes:
            if c.has_part('code_effects', 'let_manage'):
                    for u in c.user_set:
                        u.managers.add(self.user)
            if c.has_part('code_effects', 'let_manage_recursive'):
                    competitions = Competition.objects.filter(
                        competitor_code_generator__salt=c.salt,
                        competitor_code_generator__format=c.format).unique()
                    for u in c.user_set:
                        u.managers.add(self.user)
                        for competition in competitions:
                            for superior in u.__superiors(
                                    competition.administrator_code_generator):
                                u.managers.add(superior)

    def merge_to_top(self, limit=None):
        if self.merged_with is not None:
            # detect cycles, merge profiles
            profile = self
            old_profiles = set()
            old_profiles.add(None)
            while profile not in old_profiles and \
                    limit is not None and \
                    len(old_profiles) < limit:
                old_profiles.add(profile)
                prev_profile = profile
                profile = profile.merged_with
            if profile is None:
                profile = prev_profile
            elif profile in old_profiles:
                # this is a cycle. Break it.
                old_profiles.remove(profile)
                profile.merged_with = None
                profile.save()
            else:
                # limit exceeded.
                pass
            old_profiles.remove(None)
            for old_profile in old_profiles:
                old_profile.merged_with = profile
                old_profile.save()
            return profile
        # profile not merged
        return self


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        p = Profile.objects.create(user=instance)
        p.managed_profiles.add(p)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
