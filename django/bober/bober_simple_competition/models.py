from django.db import models
from django.db.models import SlugField, CharField, TextField, IntegerField, FloatField
from django.db.models import FileField, BooleanField
from django.db.models import DateTimeField
from django.db.models import ForeignKey, ManyToManyField, OneToOneField
from django.db.models import FileField, BinaryField, CommaSeparatedIntegerField
from django.db.models import signals
from django.contrib.auth.models import User
from django.core.files.base import ContentFile, File
from code_based_auth.models import Code, CodeField, CodeGenerator, CODE_COMPONENT_FORMATS, HASH_ALGORITHMS, FORMAT_FUNCTIONS, DEFAULT_COMPONENT_FORMAT, DEFAULT_HASH_ALGORITHM
from taggit.managers import TaggableManager
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from collections import OrderedDict
from . import graders
import random
import os
import json
import base64
import zipfile
from bs4 import BeautifulSoup
import mimetypes


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
    except:
        pass

USER_ROLES = (
    ('competitor', 'Competitor'),
    ('admin', 'Administrator'),
)

COMPETITOR_PRIVILEGES = (
    ('attempt', _('Participate in the competition')),
    ('attempt_before_start', _('Attempt competition before start')),
    ('results_before_end', _('See results before official end of competition')),
    ('resume_attempt', _('Resume existing attempts')),
)

CODE_EFFECTS = (
    ('let_manage', _('Allow the creator to manage the profile of anyone using this code')),
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
    # ('modify_users', _('Modify users competing using codes created by the recipient of this code')),
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

class Competition(models.Model):
    def __unicode__(self):
        s = self.slug
        s += ": " + ", ".join([i.slug for i in self.questionsets.all()])
        return s
    def get_absolute_url(self):
        return reverse('competition_detail', kwargs={'slug': str(self.slug)})
    title = CharField(max_length=256, null=True, blank=True)
    promoted = models.BooleanField(default=False)
    slug = SlugField(unique=True)
    administrator_code_generator = ForeignKey(CodeGenerator, related_name='administrator_code_competition_set')
    competitor_code_generator = ForeignKey(CodeGenerator, related_name='competitor_code_competition_set')
    questionsets = ManyToManyField('QuestionSet', through='CompetitionQuestionSet')
    start = DateTimeField()
    # duration in seconds
    duration = IntegerField(default=60*60) # 60s * 60 = 1h.
    end = DateTimeField()
 
    def expand_competitor_code(self, short_code, competition_questionset):
        sep = self.competitor_code_generator.format.separator
        return competition_questionset.slug_str() + sep + short_code
    
    def split_competitor_code(self, access_code):
        sep = self.competitor_code_generator.format.separator
        return access_code.split(sep)
    
    def grade_answers(self, grader_runtime_manager=None, 
            update_graded=False, regrade=False):
        grader_runtime_manager = graders.init_runtimes(
            grader_runtime_manager)
        if grader_runtime_manager is None:
            grader_runtime_manager = graders.RuntimeManager()
            grader_runtime_manager.start_runtimes()
        if update_graded:
            self.update_graded_answers(regrade = regrade, 
                grader_runtime_manager = grader_runtime_manager)
            if regrade:
                return
        for cq in CompetitionQuestionSet.objects.filter(competition=self):
            cq.grade_answers(grader_runtime_manager=grader_runtime_manager,
                update_graded=False, regrade=regrade)
    
    def update_graded_answers(self, regrade=False, grader_runtime_manager = None):
        grader_runtime_manager = graders.init_runtimes(
            grader_runtime_manager)
        for cq in CompetitionQuestionSet.objects.filter(competition=self):
            cq.update_graded_answers(regrade=regrade, 
                grader_runtime_manager=grader_runtime_manager)

    def admin_privilege_choices(self, access_code):
        return filter(
            lambda x: self.administrator_code_generator.code_matches(access_code,
                {'admin_privileges': [x[0]]}),
            ADMIN_PRIVILEGES)
    
    def allowed_effect_choices(self, access_code):
        return filter(
            lambda x: self.administrator_code_generator.code_matches(access_code,
                {'allowed_effects': [x[0]]}),
            CODE_EFFECTS)
    
    def competitor_privilege_choices(self, access_code):
        return filter(
        lambda x: self.administrator_code_generator.code_matches(access_code,
            {'competitor_privileges': [x[0]]}),
        COMPETITOR_PRIVILEGES)
    
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
            competition_questionset = None,
            code_data = None):
        if code_data is None:
            code_data = self.max_competitor_code_data(access_code)
        if competition_questionset is not None:
            code_data['competition_questionset'] = [competition_questionset.slug_str()]
        c = self.competitor_code_generator.create_code(code_data)
        c.save()
        return c
    def master_code_create(self):
        c = self.administrator_code_generator.create_code({
            'admin_privileges': [i[0] for i in ADMIN_PRIVILEGES],
            'competitor_privileges': [i[0] for i in COMPETITOR_PRIVILEGES],
            'allowed_effects':  [i[0] for i in CODE_EFFECTS],
        })
        c.save()
        return c
    def admin_code_create(self, access_code, code_data = None):
        if code_data is None:
            code_data = self.max_admin_code_data(access_code)
        c = self.administrator_code_generator.create_code(code_data)
        c.save()
        return c 

ANSWER_BATCH_SIZE = 100000

def _create_graded(answer, regrade, grader_runtime_manager):
    try:
        a = answer
        if regrade:
            g_a = GradedAnswer(
                attempt_id = a.attempt_id, question_id=a.question_id,
                answer = a 
            )
            q = Question.objects.get(id=g_a.question_id)
            grader = grader_runtime_manager.get_grader(
                q.verification_function, q.verification_function_type)
            g_a.score = grader(a.value, a.attempt.random_seed, q)
            return g_a
        else:
            g_a, created = GradedAnswer.objects.get_or_create(
                attempt_id=a.attempt_id, question_id=a.question_id,
                defaults={'answer': a, 'score': None})
            if not created and g_a.answer != a:
                g_a.answer = a
                g_a.score = None
                g_a.save()
    except Exception, e:
        print e
    return None

class CompetitionQuestionSet(models.Model):
    def __unicode__(self):
        return u"{}".format(self.name)

    name = models.CharField(max_length=256, null=True, blank=True)
    questionset = models.ForeignKey('QuestionSet')
    competition = models.ForeignKey('Competition')
    guest_code = ForeignKey(Code, null=True, blank=True)
 
    def slug_str(self):
        return unicode(self.id) + '.' + self.questionset.slug
    
    @classmethod
    def get_by_slug(cls, slug):
        return cls.objects.get(id=slug[:slug.find('.')])
    
    def grade_answers(self, grader_runtime_manager=None,
            update_graded=False, regrade=False):
        grader_runtime_manager = graders.init_runtimes(
            grader_runtime_manager)
        #for i in self.attempt_set.all():
        #    i.grade_answers(grader_runtime_manager = grader_runtime_manager,
        #        update_graded = update_graded, regrade=regrade)
        #return
        #the implementation below should be faster.
        if update_graded:
            self.update_graded_answers(regrade=regrade, 
                grader_runtime_manager=grader_runtime_manager)
            if regrade:
                return
        graded_answers = GradedAnswer.objects.filter(attempt__competitionquestionset=self).distinct()
        if not regrade:
            graded_answers = graded_answers.filter(score=None)
        graded_answers.select_related('question__verification_function',
            'question__verification_function_type',
            'answer__value', 'attempt')
        for g_a in graded_answers:
            # print "regrading", g_a.id, g_a.answer.id, g_a.answer
            q = g_a.question
            grader = grader_runtime_manager.get_grader(
                q.verification_function, q.verification_function_type)
            g_a.score = grader(g_a.answer.value, g_a.attempt.random_seed, q)
            g_a.save()

    def update_graded_answers(self, check_timestamp = False, 
            regrade=False, grader_runtime_manager=None):
        grader_runtime_manager = graders.init_runtimes(
            grader_runtime_manager)
        answers = Answer.objects.filter(
            attempt__competitionquestionset=self).order_by('-timestamp')
        if check_timestamp:
            answers.select_related('attempt__finish')
        if regrade:
            answers.select_related('attempt__random_seed')
            GradedAnswer.objects.filter(
                attempt__competitionquestionset=self).delete()
        graded_list = []
        grades_set = set()
        for a in answers:
            if (not check_timestamp or a.timestamp < a.attempt.finish) and (
                    (a.attempt_id, a.randomized_question_id) not in grades_set):
                g_a = _create_graded(a, regrade, grader_runtime_manager)
                if g_a:
                    graded_list.append(g_a)
                grades_set.add((a.attempt_id, a.randomized_question_id))
            if len(graded_list) > ANSWER_BATCH_SIZE:
                GradedAnswer.objects.bulk_create(graded_list)
                graded_list = []
                grades_set.clear()
        GradedAnswer.objects.bulk_create(graded_list)

class CodeEffect(models.Model):
    code = ForeignKey(Code)
    effect = models.CharField(max_length = 64, choices=CODE_EFFECTS)
    def apply(self, users=None):
        def let_manage(profile):
            for owner in self.code.owner_set:
                owner.managed_profiles.add(profile)
        def let_manage_recursive(profile):
            competitions = Competition.objects.filter(
            competitor_code_generator__salt = self.code.salt,
            competitor_code_generator__format = self.code.format).unique()
            for owner in self.code.owner_set:
                owner.managed_profiles.add(profile)
                for competition in competitions:
                    for superior in superiors(owner,
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

class ShortenedCode(models.Model):
    class Meta:
        unique_together = (('competition_questionset', 'short'),)
    def __unicode__(self):
        return u"{}: ({}) {}".format(self.short, self.competition_questionset, self.code)
    competition_questionset = ForeignKey(CompetitionQuestionSet)
    code = ForeignKey(Code, unique=True)
    short = models.CharField(max_length=64)

class QuestionSet(models.Model):
    def __unicode__(self):
        return u"{}: {}".format(self.name, ",".join([unicode(i) for i in self.questions.all()]))
    def get_absolute_url(self):
        return reverse('questionset_detail', kwargs={'pk': str(self.id)})
    slug = SlugField(unique=True)
    name = CharField(max_length = 255)
    questions = ManyToManyField('Question')
    resource_caches = ManyToManyField('ResourceCache', null=True, blank=True)

    def question_mapping(self, random_seed):
        q = self.questions.order_by('identifier').values_list('identifier')
        d = dict()
        r = random.Random(random_seed)
        c = r.sample(xrange(2**24), len(q))
        for n, i in enumerate(q):
            d[i[0]] = c[n]
        return d

    def cache_dir(self):
        return str(self.id) + "-" + self.slug

    def reverse_question_mapping(self, random_seed):
        return {v: k for k, v in self.question_mapping(random_seed).iteritems()}

    def rebuild_caches(self, embed_images = True):
        html_resources = {}
        self.resource_caches.all().delete()
        html_cache = ResourceCache(format = 'zip')
        html_cache.file.name = os.path.join("caches", self.cache_dir(), "html_cache.zip")
        html_cache.save()
        ensure_dir_exists(html_cache.file.path)
        embeded_resource_ids = []
        html_resource_zip = zipfile.ZipFile(html_cache.file.path, 'w')
        for q in self.questions.all():
            for r in q.resource_set.filter(resource_type = "html",
                part_of_solution = False):
                html_resources[q.identifier + '/' + r.relative_url] = r
                html_resource_zip.writestr(
                    q.identifier + '/' + 'Manifest.json',
                    json.dumps(q.manifest(safe = True)))
        for url, r in html_resources.iteritems():
            if embed_images:
                index_soup = BeautifulSoup(r.as_bytes())
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
                                data_res = r.question.resource_set.get(relative_url = url_str)
                                i[url_property] = "data:" + data_res.mimetype + ";base64,"  + data_res.as_base64()
                                embeded_resource_ids.append(data_res.id)
                            except Exception, e:
                                print url_str, e
                embeded_resource_ids.append(r.id)
                index_str = bytes(index_soup.prettify().encode('utf-8'))
            else:
                index_str = r.as_bytes()
            html_resource_zip.writestr(url, index_str)
            html_cache.resources.add(r)
        html_resource_zip.close()
        self.resource_caches.add(html_cache)
        for q in self.questions.all():
            for r in q.resource_set.exclude(part_of_solution = True).exclude(
                id__in = embeded_resource_ids):
                print "must create cache for ", r.id, r.question.identifier, r.file.name

class ResourceCache(models.Model):
    def __unicode__(self):
        return u"{}: {}".format(self.format, self.file)
    file = FileField(upload_to='caches')
    format = CharField(max_length = 16, choices=CACHE_FORMATS)
    resources = ManyToManyField('Resource')

class Resource(models.Model):
    def __unicode__(self):
        return u"{}: {}".format(self.relative_url, self.file)
    question = ForeignKey('Question')
    relative_url = CharField(max_length = 255)
    file = FileField(null = True, upload_to = 'resources')
    resource_type = CharField(max_length = 255)
    mimetype = CharField(max_length = 255)
    data = BinaryField(null = True)
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
            fname = os.path.join('resources', self.question.identifier, self.relative_url)
            self.file.name = fname
            ensure_dir_exists(self.file.path)
            with open(self.file.path, 'w') as f:
                f.write(self.data)
            # self.file.save(fname, ContentFile(self.data))
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


def _question_from_dirlike(cls, identifier = '-1',
        language = None,
        regenerate_modules = True, 
        regenerate_manifest = True,
        remove_correct_answer_class = True,
        my_open=None, my_path=None, my_close=None):
    question = None
    if language is None:
        language = settings.LANGUAGE_CODE.split('-')[0]
    try:
        f = my_open(my_path('Manifest.json'))
        manifest = json.load(f)
    except Exception, e:
        manifest = {'id': identifier, 
            'language': language}
        print " no manifest? ", e
        regenerate_manifest = True
    try:
        my_close(f)
    except:
        pass
    identifier = manifest['id']
    language = manifest['language']
    # get properties from database into question_dict
    try:
        question = cls.objects.filter(identifier=identifier)
        q1 = question.filter(language = language)
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
            resource_list.append({'url': resource.url, 'type': resource.resource_type})
        question_dict['task'] = resource_list
    except ObjectDoesNotExist:
        question = None
        regenerate_modules = True
    # read index
    f = my_open(my_path('index.html'))
    index_str = f.read()
    my_close(f)
    index_dict = {}
    # get properties from index
    index_dict = {}
    index_soup = BeautifulSoup(index_str)
    try:
        index_dict['title'] = unicode(index_soup.title.contents[0]).strip()
    except:
        pass
    try:
        index_dict['version'] = index_soup.find('meta', {'name':'revision'}).attrs['content']
    except:
        pass
    try:
        index_dict['country'] = index_soup.find('meta', {'name':'geo.country'}).attrs['content'].upper()
    except:
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
    for k, v in default_manifest_values.iteritems():
        if k not in manifest:
            manifest[k] = v
    if question is None:
        print "creating question", manifest['title'], type(manifest['title'])
        question = cls(country = manifest['country'], 
            slug = slugify(manifest['title']) + '-' + manifest['id'], 
            identifier = manifest['id'], title = manifest['title'],
            version = manifest['version'], authors = manifest['authors'],
            verification_function = ",".join(manifest['acceptedAnswers']))
        question.save()
    else:
        question.country = manifest['country']
        question.slug = slugify(manifest['title'] + '-' + manifest['id'])
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
            f = my_open(fname)
            data = f.read()
            my_close(f)
            r = Resource(question = question,
                relative_url = i['url'],
                file = None,
                mimetype = mimetypes.guess_type(i['url'])[0],
                resource_type = i['type'],
                data = data)
            r.save()
        except Exception, e:
            modules_list.append(i)
    return question

class Question(models.Model):
    def __unicode__(self):
        return self.title
    country = CharField(max_length = 5)
    slug = SlugField()
    identifier = CharField(max_length = 64, unique=True)
    title = TextField()
    tags = TaggableManager()
    version = CharField(max_length = 255, default='0')
    verification_function_type = IntegerField(
        choices=GRADER_FUNCTION_TYPES, default=0)
    verification_function = TextField(default="", blank=True)
    license = TextField(default="Creative commons CC-By")
    language = CharField(max_length=7, choices=settings.LANGUAGES)
    authors = TextField(default="Various")
    min_score = FloatField(default=-1)
    none_score = FloatField(default=0)
    max_score = FloatField(default=1)
    # accepted_answers = CommaSeparatedIntegerField(max_length = 255, blank=True, null=True)

    def index(self):
        for u in ['index.html', 'index.htm']:
            try:
                return self.resource_set.get(relative_url = u)
            except:
                pass
        return None

    def solution(self):
        for u in ['solution.html']:
            try:
                return self.resource_set.get(relative_url = u)
            except:
                pass
        return None

    def index_str(self, embed_resources = True):
        raw_index = self.index().as_bytes()

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
        for i in self.resource_set.filter(part_of_solution = False):
            manifest['task'].append({"type":i.resource_type, 
                'url': i.relative_url})
        if not safe:
            for i in self.resource_set.filter(part_of_solution = True):
                manifest['solution'].append({"type":i.resource_type, 
                    'url': i.relative_url})
            manifest['acceptedAnswers'] = [int(i) for i in 
                self.accepted_answers.split(',')]
        return manifest

    @classmethod
    def from_zip(cls, f, identifier = '-1',
            language = None,
            regenerate_modules = True, 
            regenerate_manifest = True,
            remove_correct_answer_class = True):
        z = zipfile.ZipFile(f)
        kwargs['my_open']=z.open
        kwargs['my_path']=lambda *x: '/'.join(x)
        kwargs['my_close']=lambda x: None
        retval = __question_from_dirlike(cls, *args, **kwargs)
        z.close()
        return retval

    @classmethod
    def from_dir(cls, dirname, *args, **kwargs):
        kwargs['my_open']=open
        kwargs['my_path']=lambda *x: os.path.join(dirname, *x)
        kwargs['my_close']=lambda x: x.close()
        return _question_from_dirlike(cls, *args, **kwargs)

class Answer(models.Model):
    def __unicode__(self):
        #print self.correct()
        return "{} ({}): {}".format(
            unicode(self.attempt.reverse_question_mapping().get(
                self.randomized_question_id, "??")),
            unicode(self.randomized_question_id),
            unicode(self.value))
            
    attempt = ForeignKey('Attempt')
    randomized_question_id = IntegerField()
    timestamp = DateTimeField(auto_now_add = True)
    value = TextField(blank=True, null = True)
    score = FloatField(null=True)

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


class AttemptInvalidation(models.Model):
    by = ForeignKey('Profile')
    reason = TextField(blank=True)

class AttemptConfirmation(models.Model):
    def __unicode__(self):
        return u"{}: {}".format(by, attempt)
    by = ForeignKey('Profile')
    attempt = ForeignKey('Attempt')

class Competitor(models.Model):
    def __unicode__(self):
        return u"{} {} ({})".format(self.first_name, self.last_name,
            self.profile or '?')
    profile = ForeignKey('Profile', null=True, blank=True)
    first_name = models.CharField(max_length=128, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=128, verbose_name=_("Last Name"))

class GradedAnswer(models.Model):
    attempt = ForeignKey('Attempt')
    question = ForeignKey('Question')
    answer = ForeignKey('Answer')
    score = FloatField(null=True)
 
class Attempt(models.Model):
    def __unicode__(self):
        return u"{}: {} - {}: {} ({} - {})".format(self.competitor,
            self.competition.slug,
            self.questionset.name,
            self.access_code,
            self.start, self.finish)

    access_code = CodeField()
    competitionquestionset = ForeignKey('CompetitionQuestionSet')
    # user = ForeignKey('Profile', null=True, blank=True)
    competitor = ForeignKey('Competitor', null=True, blank=True)
    invalidated_by = ForeignKey('AttemptInvalidation', null=True, blank=True)
    confirmed_by = ManyToManyField('Profile', through='AttemptConfirmation',
        null=True, blank=True)
    random_seed = IntegerField()
    start = DateTimeField(auto_now_add = True)
    finish = DateTimeField(null=True, blank=True)
    score = FloatField(null=True, blank=True)
    #graded_answers = ManyToManyField('Answer', through='GradedAnswer',
    #    related_name = 'graded_attempt',
    #    null=True, blank=True)
 
    @property
    def competition(self):
        return self.competitionquestionset.competition
    
    @property
    def questionset(self):
        return self.competitionquestionset.questionset
    
    @property
    def valid(self):
        return self.invalidated_by == None
    
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
                regrade = regrade)
            if regrade:
                return
        graded_answers = self.gradedanswer_set.all()
        if not regrade:
            graded_answers = graded_answers.filter(score=None)
        graded_answers.select_related('question', 'answer__value')
        for g_a in graded_answers:
            # print "    regrading", g_a.answer
            q = g_a.question
            grader = grader_runtime_manager.get_grader(
                q.verification_function, q.verification_function_type)
            g_a.score = grader(g_a.answer.value, self.random_seed, q)
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
        answers = self.answer_set.order_by("-timestamp")
        if check_timestamp:
            answers = answers.filter(timestamp__lte=self.finish)
        n_questions = self.questionset.questions.count()
        n_found = 0
        for a in answers.all():
            # print "a:", a
            if a.randomized_question_id not in answered_questions:
                g_a = _create_graded(a, regrade, grader_runtime_manager)
                answered_questions.add(a.randomized_question_id)
                if g_a:
                    graded_list.append(g_a)
                n_found += 1
                if n_found >= n_questions:
                    break
        GradedAnswer.objects.bulk_create(graded_list)

    def latest_answers(self):
        # get only the latest answers
        return self.gradedanswer_set.all()

    def graded_answers_by_question_id(self):
        # return self.graded_answers.order_by('gradedanswer__question_id')
        answered_questions = OrderedDict()
        # print "loading."
        for q_id in self.questionset.questions.all().order_by('id').values_list(
                'id', flat=True):
            answered_questions[q_id] = self.gradedanswer_set.filter(
                question_id = q_id).first()
        return answered_questions
        #n_questions = len(answered_questions)
        #n_found = 0
        # print "  iterating.."
        #for a in self.answer_set.order_by("-timestamp"):
        #    q_id = a.question_id
        #    if answered_questions[q_id] is None:
        #        answered_questions[q_id] = a
        #        n_found += 1
        #        if n_found >= n_questions:
        #            # print "  ", answered_questions
        #            return answered_questions
        # print "  ", answered_questions
        #return answered_questions
    
    def latest_answers_sum(self):
        return int(sum([a.score for a in self.gradedanswer_set.all() if a.score is not None]))


class Profile(models.Model):
    def __unicode__(self):
        return unicode(self.user)
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': str(self.pk)})
    user = models.OneToOneField(User)
    feature_level = IntegerField(choices=FEATURE_LEVELS, default=1)
    managed_profiles = models.ManyToManyField('Profile', related_name='managers', null=True, blank=True)
    # managed_users = models.ManyToManyField(User, related_name='managers', null=True, blank=True)
    #first_competition = models.ForeignKey(Competition, null=True, blank=True)
    #registration_code = CodeField(null=True, blank=True)
    created_codes = ManyToManyField(Code, null=True, blank=True,
        related_name='creator_set')
    received_codes = ManyToManyField(Code, null=True, blank=True,
        related_name='recipient_set')
    used_codes = ManyToManyField(Code, null=True, blank=True,
        related_name='user_set')
    question_sets = ManyToManyField(QuestionSet, null=True, blank=True)
    created_question_sets = ManyToManyField(QuestionSet, null=True, blank=True, 
        related_name='creator_set')
    questions = ManyToManyField(Question, null=True, blank=True)
    merged_with = ForeignKey('Profile', null = True, blank=True, related_name='former_profile_set')
    # merged_with = ForeignKey(User, null = True, blank=True, related_name='merged_set')
    update_used_codes_timestamp = DateTimeField(null=True, blank=True)
    update_managers_timestamp = DateTimeField(null=True, blank=True)
    vcard = models.TextField(blank=True)
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
        for c in self.received_codes.filter(format = codegen.format,
                salt = codegen.salt):
            for o in c.owner_set.all():
                if o not in known:
                    s1 = superiors(o, codegen, known)
                    known = s1.union(known)
                    known.add(o)
        return known

    def update_used_codes(self):
        if self.update_used_codes_timestamp is None:
            attempts = self.attempt_set.all()
        else:
            attempts = self.attempt_set.filter(
                start__gte = self.update_used_codes_timestamp)
            self.update_used_codes_timestamp = timezone.now()
        for a in attempts:
            try:
                codegen = a.competitionquestionset.competition.competitor_code_generator
                codes = Code.objects.filter(
                    value = a.access_code, 
                    salt = codegen.salt,
                    format = codegen.format
                )
                for c in codes:
                    used_codes.add(c)
            except Exception, e:
                print e
                pass
    def apply_code_effects(self, codes = None):
        if codes is None:
            update_managers_timestamp = timezone.now()
            codes = self.used_codes
        for c in codes:
            for effect in c.code_effect_set:
                effect.apply(users=[self])

    def update_managers(self, codes = None):
        for c in codes:
            if c.format.code_matches(c.salt,
                c.value, {'code_effects': ['let_manage']}):
                    for u in c.owner_set:
                        u.managed_profiles.add(self)
            if c.format.code_matches(c.salt,
                c.value, {'code_effects': ['let_manage_recursive']}):
                    competitions = Competition.objects.filter(
                        competitor_code_generator__salt = c.salt,
                        competitor_code_generator__format = c.format).unique()
                    for u in c.owner_set:
                        u.managed_profiles.add(self)
                        for competition in competitions:
                            for superior in superiors(u,
                                    competition.administrator_code_generator):
                                superior.managed_profiles.add(self)

    def update_managed_profiles(self, codes = None):
        if codes is None:
            codes = Code.objects.filter(owner_set = self).unique()
        for c in codes:
            if c.format.code_matches(c.salt,
                c.value, {'code_effects': ['let_manage']}):
                    for u in c.user_set:
                        u.managers.add(self.user)
            if c.format.code_matches(c.salt,
                c.value, {'code_effects': ['let_manage_recursive']}):
                    competitions = Competition.objects.filter(
                        competitor_code_generator__salt = c.salt,
                        competitor_code_generator__format = c.format).unique()
                    for u in c.user_set:
                        u.managers.add(self.user)
                        for competition in competitions:
                            for superior in u.__superiors(
                                    competition.administrator_code_generator):
                                u.managers.add(superior)

 
def create_profile(sender, instance=None, **kwargs):
    try:
        p = instance.profile
    except Profile.DoesNotExist:
        p = Profile()
        p.user = instance
        p.save()

signals.post_save.connect(create_profile, sender=User)
