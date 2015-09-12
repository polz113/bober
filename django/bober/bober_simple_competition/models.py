from django.db import models
from django.db.models import SlugField, CharField, TextField, IntegerField
from django.db.models import FileField, BooleanField
from django.db.models import DateTimeField
from django.db.models import ForeignKey, ManyToManyField, OneToOneField
from django.db.models import FileField, BinaryField, CommaSeparatedIntegerField
from django.db.models import signals
from django.contrib.auth.models import User
from django.core.files.base import ContentFile, File
from code_based_auth.models import Code, CodeField, CodeGenerator
from taggit.managers import TaggableManager
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext as _
from django.utils import timezone
import random
import os
import json
import base64
import zipfile
from bs4 import BeautifulSoup
import mimetypes


# Create your models here.
VERIFICATION_FUNCTION_TYPES = (
    (0, 'internal'),
    (1, 'javascript'),
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
)

CODE_EFFECTS = (
    ('let_manage', _('Allow the creator to manage the profile of anyone using this code')),
    ('let_manage_recursive', _('Allow the creator and their managers to manage the profile of anyone using this code')),
    ('new_attempt', _('Start a new attempt every time this code is used')),
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


class Competition(models.Model):
    def __unicode__(self):
        s = self.slug
        s += ": " + ", ".join([i.slug for i in self.questionsets.all()])
        return s
    def get_absolute_url(self):
        return reverse('competition_detail', kwargs={'slug': str(self.slug)})
    slug = SlugField(unique=True)
    administrator_code_generator = ForeignKey(CodeGenerator, related_name='administrator_code_competition_set')
    competitor_code_generator = ForeignKey(CodeGenerator, related_name='competitor_code_competition_set')
    questionsets = ManyToManyField('QuestionSet', through='CompetitionQuestionSet')
    start = DateTimeField()
    # duration in seconds
    duration = IntegerField(default=60*60) # 60s * 60 = 1h.
    end = DateTimeField()

class CompetitionQuestionSet(models.Model):
    def __unicode__(self):
        return u"{}: {} ({})".format(self.id, self.name, self.questionset.slug)
    name = models.CharField(max_length=256, null=True, blank=True)
    questionset = models.ForeignKey('QuestionSet')
    competition = models.ForeignKey('Competition')
    guest_code = ForeignKey(Code, null=True, blank=True)

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
    resource_set = set()
    imgs = index_soup.find_all('img')
    objs = index_soup.find_all('object')
    scripts = index_soup.find_all('script')
    for items, item_type, url_property in [
        (imgs, 'image', 'src'), 
        (objs, 'image', 'data'), 
        (scripts, 'javascript', 'src')]:
        for i in items:
            url = i.get(url_property, None)
            if url is not None:
                resource_set.add((item_type, url))
    resource_list = [
        {'type': item_type, 'url': url} for item_type, url in resource_set
    ]
    index_dict['task'] = [
        {'type': "html", "url": "index.html"}] + resource_list
    if regenerate_manifest:
        manifest.update(index_dict)
    if regenerate_modules:
        manifest['task'] = index_dict['task']
    if question is None:
        print "creating question", manifest['title'], type(manifest['title'])
        question = cls(country = manifest['country'], 
            slug = slugify(manifest['title']) + '-' + manifest['id'], 
            identifier = manifest['id'], title = manifest['title'],
            version = manifest['version'], authors = manifest['authors'],
            accepted_answers = ",".join(manifest['acceptedAnswers']))
        question.save()
    else:
        question.country = manifest['country']
        question.slug = slugify(manifest['title'] + '-' + manifest['id'])
        question.title = manifest['title']
        question.version = manifest['version']
        question.authors = manifest['authors']
        question.accepted_answers = ",".join(manifest['acceptedAnswers'])
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
        choices=VERIFICATION_FUNCTION_TYPES, default=0)
    verification_function = TextField(default="", blank=True)
    license = TextField(default="Creative commons CC-By")
    language = CharField(max_length=7, choices=settings.LANGUAGES)
    authors = TextField(default="Various")
    accepted_answers = CommaSeparatedIntegerField(max_length = 255, blank=True, null=True)
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
    timestamp = DateTimeField(auto_now = True)
    value = IntegerField(null = True)
    @property
    def question(self):
        return Question.objects.get(identifier=self.question_id)
    @property
    def question_id(self):
        return self.attempt.reverse_question_id(
            self.randomized_question_id)
    def correct(self):
        if self.value is None:
            return None
        return str(self.value) in self.question.accepted_answers.split(',')

class AttemptInvalidation(models.Model):
    by = ForeignKey('Profile')
    reason = TextField(blank=True)

class Attempt(models.Model):
    def __unicode__(self):
        return "{}: {} - {}: {} ({} - {})".format(self.user,
            self.competition.slug,
            self.questionset.name,
            self.access_code,
            self.start, self.finish)
    access_code = CodeField()
    competitionquestionset = ForeignKey('CompetitionQuestionSet')
    user = ForeignKey('Profile', null=True, blank=True)
    invalidated_by = ForeignKey('AttemptInvalidation', null=True, blank=True)
    random_seed = IntegerField()
    start = DateTimeField(auto_now_add = True)
    finish = DateTimeField(null=True, blank=True)
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
    def latest_answers(self):
        # get only the latest answers
        answered_questions = set()
        answers = []
        n_questions = self.questionset.questions.count()
        n_found = 0
        for a in self.answer_set.order_by("-timestamp"):
            if a.randomized_question_id not in answered_questions:
                answers.append(a)
                answered_questions.add(a.randomized_question_id)
                n_found += 1
                if n_found >= n_questions:
                    return answers
        return answers


class Profile(models.Model):
    def __unicode__(self):
        return unicode(self.user)
    def get_absolute_url(self):
        return reverse('competition_detail', kwargs={'pk': str(self.pk)})
    user = models.OneToOneField(User)
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
    merged_with = ForeignKey('Profile', null = True, blank=True, related_name='former_profile_set')
    # merged_with = ForeignKey(User, null = True, blank=True, related_name='merged_set')
    update_used_codes_timestamp = DateTimeField(null=True, blank=True)
    update_managers_timestamp = DateTimeField(null=True, blank=True)
    vcard = models.TextField(blank=True)

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

    def update_managers(self, codes = None):
        if codes is None:
            update_managers_timestamp = timezone.now()
            codes = self.used_codes
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
