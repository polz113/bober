from django.db import models
from bober_simple_competition.models import Profile, ShortenedCode, CompetitionQuestionSet, Competition
from code_based_auth.models import Code
from django.utils.translation import ugettext as _

# Create your models here.

SCHOOL_CATEGORIES = (
    ('ELEMENTARY', _('Elementary school')),
    ('HIGHSCHOOL', _('High school')),
    ('KINDERGARDEN', _('Kindergarden')),
)

class School(models.Model):
    def __unicode__(self):
        return u"{}, {} ({})".format(self.name, self.post, self.category)
    name = models.CharField(unique=True, max_length=255)
    category = models.CharField(choices=SCHOOL_CATEGORIES, max_length=24)
    address = models.CharField(max_length=1024, blank=True, null=True)
    country_code = models.CharField(max_length = 2)
    postal_code = models.IntegerField(blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    tax_number = models.CharField(max_length=12, blank=True, null=True)
    identifier = models.CharField(max_length=20, blank=True, null=True)
    headmaster = models.CharField(max_length=255, blank=True, null=True)

class SchoolTeacherCode(models.Model):
    def __unicode__(self):
        return u"{} {}:{}".format(self.school, self.teacher, self.code)
    school = models.ForeignKey(School)
    teacher = models.ForeignKey(Profile)
    code = models.ForeignKey(Code)


class SchoolCategoryQuestionSets(models.Model):
    def __unicode__(self):
        return u"{} {}".format(self.competition, self.school_category)
    class Meta:
        unique_together = (("competition", "school_category"))
    competition = models.ForeignKey(Competition)
    questionsets = models.ManyToManyField(CompetitionQuestionSet)
    school_category = models.CharField(choices=SCHOOL_CATEGORIES, max_length=24)

class SchoolCompetition(Competition):
    class Meta:
        proxy = True
    def questionsets_for_school_category(self, school_category):
        try:
            return SchoolCategoryQuestionSets.objects.get(
                    school_category = school_category, competition=self
                ).questionsets.all()
        except Exception, e:
            pass
        return CompetitionQuestionSet.objects.none()
            
    def school_codes_create(self, school, teacher, access_code,
            code_data = None):
        for cqs in self.questionsets_for_school_category(
                school_category = school.category):
            if code_data is not None:
                code_data['competition_questionset'] = cqs.slug_str()
            self.school_code_create(school, teacher, access_code, 
                competition_questionset = cqs, code_data = code_data)
    def school_code_create(self, school, teacher, access_code, 
            competition_questionset = None,
            code_data=None):
        code = self.competitor_code_create(
            access_code, competition_questionset = competition_questionset,
            code_data = code_data)
        teacher.created_codes.add(code)
        sc = SchoolTeacherCode(teacher=teacher, school=school, 
            code=code)
        sc.save()
