# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
import hashlib
import datetime
from django.db import models

class Yiisession(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    expire = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'YiiSession'

class Award(models.Model):
    id = models.AutoField(primary_key=True)
    competition_user = models.ForeignKey('CompetitionUser', related_name='award_back')
    type = models.IntegerField()
    serial = models.CharField(unique=True, max_length=255)
    class Meta:
        managed = False
        db_table = 'award'

class Competition(models.Model):
    def __unicode__(self):
        return u"{0}".format(self.name)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    active = models.IntegerField()
    timestamp_start = models.DateTimeField()
    timestamp_stop = models.DateTimeField()
    type = models.IntegerField()
    public_access = models.IntegerField()
    duration = models.IntegerField()
    timestamp_mentor_results = models.DateTimeField(blank=True, null=True)
    timestamp_mentor_awards = models.DateTimeField(blank=True, null=True)
    timestamp_mentor_advancing_to_next_level = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'competition'

class CompetitionCategory(models.Model):
    def __unicode__(self):
        return u"{0}".format(self.name)
    id = models.AutoField(primary_key=True)
    active = models.IntegerField()
    country = models.ForeignKey('Country')
    name = models.CharField(max_length=255)
    level_of_education = models.IntegerField()
    class_from = models.IntegerField()
    class_to = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'competition_category'

class CompetitionCategoryActive(models.Model):
    id = models.AutoField(primary_key=True)
    competition = models.ForeignKey(Competition)
    competition_category = models.ForeignKey(CompetitionCategory)
    number_of_questions = models.IntegerField(blank=True, null=True)
    minimum_points_for_bronze_award = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    maximum_bronze_awards = models.IntegerField()
    minimum_points_for_silver_award = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    maximum_silver_awards = models.IntegerField()
    minimum_points_for_gold_award = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    maximum_gold_awards = models.IntegerField()
    total_contestants_to_advance_to_next_level = models.IntegerField()
    available_contest_time = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'competition_category_active'

class CompetitionCategorySchool(models.Model):
    def __unicode__(self):
        return u"{0}: {1}".format(self.school, self.competition_category)
    id = models.AutoField(primary_key=True)
    competition = models.ForeignKey(Competition)
    competition_category = models.ForeignKey(CompetitionCategory)
    school = models.ForeignKey('School')
    class Meta:
        managed = False
        db_table = 'competition_category_school'

class CompetitionCategorySchoolMentor(models.Model):
    def __unicode__(self):
        if self.disqualified:
            disqualified_str = u"X(by {0})".format(self.disqualified_by)
        else:
            disqualified_str = u''
        return u"{0} - {1}: {2}".format(self.user, self.competition_category_school, self.access_code)+disqualified_str
    id = models.AutoField(primary_key=True)
    competition_category_school = models.ForeignKey(CompetitionCategorySchool)
    user = models.ForeignKey('Users', related_name = 'competition_category_school_mentor_set')
    access_code = models.CharField(unique=True, max_length=20, blank=True)
    disqualified = models.IntegerField()
    disqualified_by = models.ForeignKey('Users', related_name = 'disqualified_set', db_column='disqualified_by', blank=True, null=True)
    disqualified_reason = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'competition_category_school_mentor'

class CompetitionCategoryTranslation(models.Model):
    id = models.AutoField(primary_key=True)
    competition_category = models.ForeignKey(CompetitionCategory)
    language = models.ForeignKey('Language')
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'competition_category_translation'

class CompetitionCommittee(models.Model):
    id = models.AutoField(primary_key=True)
    competition = models.ForeignKey(Competition)
    user = models.ForeignKey('Users')
    president = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'competition_committee'

class CompetitionCountry(models.Model):
    id = models.AutoField(primary_key=True)
    competition = models.ForeignKey(Competition)
    country = models.ForeignKey('Country')
    class Meta:
        managed = False
        db_table = 'competition_country'

class CompetitionQuestion(models.Model):
    def __unicode__(self):
        return u"{} - {}".format(self.competition, self.question)
    id = models.AutoField(primary_key=True)
    competition = models.ForeignKey(Competition)
    question = models.ForeignKey('Question')
    class Meta:
        managed = False
        db_table = 'competition_question'

class CompetitionQuestionCategory(models.Model):
    def __unicode__(self):
        return u"{} - {}({})".format(self.competition_category, self.competition_question, self.competiton_question_difficulty)
    id = models.AutoField(primary_key=True)
    competition_question = models.ForeignKey(CompetitionQuestion)
    competition_category = models.ForeignKey(CompetitionCategory)
    competiton_question_difficulty = models.ForeignKey('CompetitionQuestionDifficulty')
    class Meta:
        managed = False
        db_table = 'competition_question_category'

class CompetitionQuestionDifficulty(models.Model):
    def __unicode__(self):
        return unicode(self.name)
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey('Country')
    active = models.IntegerField()
    name = models.CharField(max_length=255)
    correct_answer_points = models.DecimalField(max_digits=10, decimal_places=4)
    wrong_answer_points = models.DecimalField(max_digits=10, decimal_places=4)
    class Meta:
        managed = False
        db_table = 'competition_question_difficulty'

class CompetitionQuestionDifficultyTranslation(models.Model):
    id = models.AutoField(primary_key=True)
    competition_question_difficulty = models.ForeignKey(CompetitionQuestionDifficulty)
    language = models.ForeignKey('Language')
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        verbose_name = 'c_q_difficulty_translation'
        db_table = 'competition_question_difficulty_translation'

class CompetitionTranslation(models.Model):
    id = models.AutoField(primary_key=True)
    competition = models.ForeignKey(Competition)
    language = models.ForeignKey('Language')
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'competition_translation'

class CompetitionUser(models.Model):
    id = models.AutoField(primary_key=True)
    competition = models.ForeignKey(Competition)
    competition_category = models.ForeignKey(CompetitionCategory)
    user = models.ForeignKey('Users', blank=True, null=True)
    competition_category_school_mentor = models.ForeignKey(CompetitionCategorySchoolMentor, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    gender = models.IntegerField()
    class_field = models.CharField(db_column='class', max_length=20, blank=True) # Field renamed because it was a Python reserved word.
    school = models.ForeignKey('School')
    disqualified_request = models.IntegerField()
    disqualified_request_by = models.ForeignKey('Users', related_name='disqualified_request_set', db_column='disqualified_request_by', blank=True, null=True)
    disqualified = models.IntegerField()
    disqualified_by = models.ForeignKey('Users', related_name = 'disqualified_competition_user_set', db_column='disqualified_by', blank=True, null=True)
    disqualified_reason = models.TextField(blank=True)
    advancing_to_next_level = models.IntegerField()
    award = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    finished = models.IntegerField()
    total_points_via_answers = models.DecimalField(max_digits=10, decimal_places=4)
    total_points_via_time = models.DecimalField(max_digits=10, decimal_places=4)
    total_points_manual = models.DecimalField(max_digits=10, decimal_places=4)
    total_points = models.DecimalField(max_digits=10, decimal_places=4)
    ip_start = models.CharField(max_length=15, blank=True)
    ip_stop = models.CharField(max_length=15, blank=True)
    class Meta:
        managed = False
        db_table = 'competition_user'

class CompetitionUserQuestion(models.Model):
    def __unicode__(self):
        return u'{} u:{} q:{} a:{} t:{}'.format(self.id, self.competition_user_id, self.competition_question_id, self.custom_answer, self.last_change)
    id = models.AutoField(primary_key=True)
    competition_user = models.ForeignKey(CompetitionUser)
    competition_question = models.ForeignKey(CompetitionQuestion)
    ordering = models.IntegerField()
    question_answer = models.ForeignKey('QuestionAnswer', blank=True, null=True)
    last_change = models.DateTimeField(blank=True, null=True)
    random_seed = models.DecimalField(max_digits=11, decimal_places=10)
    custom_answer = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'competition_user_question'

class CompetitionUserQuestionAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    competition_user_question = models.ForeignKey(CompetitionUserQuestion)
    question_answer = models.ForeignKey('QuestionAnswer')
    ordering = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'competition_user_question_answer'

class Country(models.Model):
    def __unicode__(self):
        return unicode(self.country)
    id = models.AutoField(primary_key=True)
    country = models.CharField(unique=True, max_length=255)
    class Meta:
        managed = False
        db_table = 'country'

class CountryAdministrator(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country)
    user = models.ForeignKey('Users')
    class Meta:
        managed = False
        db_table = 'country_administrator'

class CountryLanguage(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country)
    language = models.ForeignKey('Language')
    class Meta:
        managed = False
        db_table = 'country_language'

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    short = models.CharField(max_length=5)
    class Meta:
        managed = False
        db_table = 'language'

class Municipality(models.Model):
    def __unicode__(self):
        return unicode(name)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)
    class Meta:
        managed = False
        db_table = 'municipality'

class Profiles(models.Model):
    def __unicode__(self):
        return u"{0}: {1} {2}".format(self.user, self.first_name, self.last_name)
    user = models.ForeignKey('Users', primary_key=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    language = models.ForeignKey(Language, blank=True, null=True)
    user_role = models.IntegerField()
    timezone = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'profiles'

class ProfilesFields(models.Model):
    id = models.AutoField(primary_key=True)
    varname = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50)
    field_size = models.IntegerField()
    field_size_min = models.IntegerField()
    required = models.IntegerField()
    match = models.CharField(max_length=255)
    range = models.CharField(max_length=255)
    error_message = models.CharField(max_length=255)
    other_validator = models.TextField(blank=True)
    default = models.CharField(max_length=255)
    widget = models.CharField(max_length=255)
    widgetparams = models.TextField(blank=True)
    position = models.IntegerField()
    visible = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'profiles_fields'

class Question(models.Model):
    def __unicode__(self):
        return u"{}:{}".format(self.identifier, self.title)
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country)
    identifier = models.CharField(max_length=255)
    type = models.IntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    data = models.TextField(blank=True)
    version = models.CharField(max_length=255, blank=True)
    verification_function_type = models.IntegerField(blank=True, null=True)
    verification_function = models.TextField(blank=True)
    last_change_date = models.DateTimeField(blank=True, null=True)
    authors = models.TextField(blank=True)
    css = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'question'

class QuestionAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question)
    type = models.IntegerField()
    value = models.TextField()
    class Meta:
        managed = False
        db_table = 'question_answer'

class QuestionAnswerTranslation(models.Model):
    id = models.AutoField(primary_key=True)
    question_answer = models.ForeignKey(QuestionAnswer)
    language = models.ForeignKey(Language)
    value = models.TextField()
    class Meta:
        managed = False
        db_table = 'question_answer_translation'

class QuestionResource(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question)
    language = models.ForeignKey(Language)
    type = models.IntegerField()
    path = models.CharField(max_length=250)
    filename = models.CharField(max_length=250)
    file_type = models.CharField(max_length=255, blank=True)
    data = models.TextField()
    start_up = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'question_resource'

class QuestionTranslation(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question)
    language = models.ForeignKey(Language)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    data = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'question_translation'

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)
    class Meta:
        managed = False
        db_table = 'region'

class School(models.Model):
    def __unicode__(self):
        return u"{0}".format(self.name)
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    school_category = models.ForeignKey('SchoolCategory')
    level_of_education = models.IntegerField()
    address = models.CharField(max_length=255, blank=True)
    post = models.CharField(max_length=255, blank=True)
    postal_code = models.IntegerField(blank=True, null=True)
    municipality = models.ForeignKey(Municipality, blank=True, null=True)
    region = models.ForeignKey(Region, blank=True, null=True)
    country = models.ForeignKey(Country)
    tax_number = models.CharField(max_length=12, blank=True)
    identifier = models.CharField(max_length=20, blank=True)
    headmaster = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'school'

class SchoolCategory(models.Model):
    def __unicode__(self):
        return unicode(self.name)
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    active = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'school_category'

class SchoolMentor(models.Model):
    def __unicode__(self):
        return u"{}: {}".format(self.user, self.school)
    def activate(self, by_user):
        self.active = 1
        self.activated_by = by_user
        self.activated_timestamp = datetime.datetime.now()
    id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School)
    user = models.ForeignKey('Users')
    active = models.IntegerField()
    activated_by = models.ForeignKey('Users', related_name='activated_set', db_column='activated_by', blank=True, null=True)
    activated_timestamp = models.DateTimeField(blank=True, null=True)
    coordinator = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'school_mentor'

class Users(models.Model):
    def __unicode__(self):
    	return u"{0}:{1}".format(self.username, self.email)
    def set_password(self, password):
        self.password = hashlib.sha512(password).hexdigest()
    def check_password(self, password):
        return self.password == hashlib.sha512(password).hexdigest()
    @property
    def profile(self):
        return self.profiles_set.all()[0];
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=128)
    email = models.CharField(unique=True, max_length=128)
    activkey = models.CharField(max_length=128)
    createtime = models.IntegerField()
    lastvisit = models.IntegerField()
    superuser = models.IntegerField()
    status = models.IntegerField()
    create_at = models.DateTimeField()
    lastvisit_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'users'

