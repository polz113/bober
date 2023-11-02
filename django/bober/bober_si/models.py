from django.db import models
from bober_simple_competition.models import Profile, CompetitionQuestionSet, Competition, Attempt
from code_based_auth.models import Code
from django.db.models import F, Sum
from django.utils.translation import gettext as _
import os
import traceback


SCHOOL_CATEGORIES = (
    ('ELEMENTARY', _('Elementary school')),
    ('HIGHSCHOOL', _('High school')),
    ('KINDERGARDEN', _('Kindergarden')),
)

AWARD_TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'award_templates')


def assign_attempt_awards(attempt, awards, data, commit=False):
    to_revoke = []
    to_create = []
    revoked_by = data.get('revoked_by', None)
    school_name = data.get('school_name', None)
    competitor_name = u"{} {}".format(
        attempt.competitor.first_name,
        attempt.competitor.last_name)
    to_assign = set(awards)
    aawards = attempt.attemptaward_set.all()
    serials = set(aawards.values_list('serial', flat=True))
    not_needed = set()
    for award in to_assign:
        not_needed = not_needed.union(award.replaces.all())
    for aaward in aawards:
        if aaward.award in to_assign and aaward.award not in not_needed:
            if aaward.competitor_name == competitor_name and \
                    aaward.school_name == school_name and \
                    aaward.group_name == aaward.award.group_name and \
                    aaward.revoked_by is None:
                to_assign.discard(aaward.award)
            else:
                if aaward.revoked_by is None:
                    aaward.revoked_by = revoked_by
                    to_revoke.append(aaward)
        else:
            if aaward.revoked_by is None:
                aaward.revoked_by = revoked_by
                to_revoke.append(aaward)
    for award in to_assign:
        if award in not_needed:
            continue
        serial = "{}{:06}".format(award.serial_prefix, attempt.id)
        new_serial = serial
        i = 1
        while new_serial in serials:
            new_serial = "{}-{}".format(serial, i)
            i += 1
        to_create.append(AttemptAward(
                award=award,
                attempt=attempt,
                competitor_name=competitor_name,
                school_name=school_name,
                group_name=award.group_name,
                serial=new_serial,
        ))
    if commit:
        if school_name is not None:
            AttemptAward.objects.bulk_create(to_create)
            to_create = []
        if revoked_by is not None:
            AttemptAward.objects.filter(id__in=[a.id for a in to_revoke]).update(
                revoked_by=revoked_by)
            to_revoke = []
    return to_create, to_revoke


class School(models.Model):
    def __str__(self):
        return u"{}, {}".format(self.name, self.post, self.category)

    name = models.CharField(max_length=255)
    display_name = models.TextField(max_length=255)
    category = models.CharField(choices=SCHOOL_CATEGORIES, max_length=24)
    address = models.CharField(max_length=1024, blank=True, null=True)
    country_code = models.CharField(max_length=2)
    postal_code = models.IntegerField(blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    tax_number = models.CharField(max_length=12, blank=True, null=True)
    identifier = models.CharField(max_length=20, blank=True, null=True)
    headmaster = models.CharField(max_length=255, blank=True, null=True)

    def competitionquestionset_attempts(self, cqs, confirmed=True):
        if confirmed:
            attempts = Attempt.objects.filter(
                attemptconfirmation__by__schoolteachercode__school=self,
                attemptconfirmation__by__schoolteachercode__code__value=F('access_code'),
                competition_questionset=cqs).distinct()
        else:
            school_access_codes = self.schoolteachercode_set.filter(
                    code__value__startswith=cqs.slug_str()
                ).values_list(
                    'code__value', flat=True
                ).distinct()
            attempts = Attempt.objects.filter(
                competition_questionset=cqs,
                access__code__in=school_access_codes
            )
        return attempts

    def assign_si_awards(self, awards, competition_questionsets=None,
                         revoked_by=None, commit=True):
        new_awards = []
        revoke_awards = []
        for cqs in competition_questionsets.all():
            try:
                bronze_award = cqs.award_set.get(name='bronasto')
                general_award = cqs.award_set.get(name='priznanje')
                max_score = cqs.questionset.questions.all().aggregate(
                    Sum('max_score'))['max_score__sum']
                attempts = Attempt.objects.filter(
                    competitionquestionset=cqs,
                    attemptconfirmation__by__schoolteachercode__school=self,
                    attemptconfirmation__by__schoolteachercode__code__value=F('access_code'),
                    attemptconfirmation__by__schoolteachercode__competition_questionset=cqs,
                ).order_by(
                    '-score'
                ).select_related(
                    'competitor',
                ).prefetch_related(
                    'attemptaward_set',
                    'attemptaward_set__award'
                ).distinct()
                if attempts.count() < 1:
                    continue
                my_l = [a.score for a in attempts.all()]
                bronze_threshold = max(my_l[(len(my_l) - 1) // 3], bronze_award.min_threshold)
                bronze_threshold = min(bronze_threshold, bronze_award.threshold)
                for attempt in attempts:
                    to_assign = set()
                    for existing_award in attempt.attemptaward_set.filter(revoked_by=None):
                        if existing_award.award.min_threshold >= attempt.score:
                            to_assign.add(existing_award.award)
                    if attempt.score >= bronze_threshold:
                        to_assign.add(bronze_award)
                    else:
                        to_assign.discard(bronze_award)
                    for award in awards.filter(questionset=attempt.competitionquestionset):
                        if attempt.score >= max(award.threshold, award.min_threshold):
                            to_assign.add(award)
                    to_create, to_revoke = assign_attempt_awards(
                            attempt, to_assign,
                            {'revoked_by': revoked_by, 'school_name': self.display_name},
                            commit=False)
                    new_awards += to_create
                    revoke_awards += to_revoke
            except Exception as e:
                # TODO: handle exception
                pass
        if commit:
            assert revoked_by is not None
            revoked_award_ids = [a.id for a in revoke_awards]
            AttemptAward.objects.filter(id__in=revoked_award_ids).update(
                revoked_by=revoked_by)
            AttemptAward.objects.bulk_create(new_awards)
        return new_awards, revoke_awards


class SchoolTeacherCode(models.Model):
    def __str__(self):
        return u"{} {}:{}".format(self.school, self.teacher, self.code)

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
    competition_questionset = models.ForeignKey(
        CompetitionQuestionSet, null=True, on_delete=models.CASCADE)
    code = models.ForeignKey(Code, on_delete=models.CASCADE)

    def attempts(self, confirmed=True):
        a = Attempt.objects.filter(
            competitionquestionset=self.competition_questionset,
            access_code=self.code.value,
        )
        if confirmed:
            a = a.filter(confirmed_by=self.teacher)
        return a.distinct()

    def assign_si_awards(self, revoked_by=None):
        if revoked_by is None:
            revoked_by = self.teacher
        cqs = CompetitionQuestionSet.objects.filter(schoolteachercode=self)
        awards = Award.objects.filter(questionset__schoolteachercode=self).distinct()
        self.school.assign_si_awards(awards, cqs, revoked_by)

    def attempt_awards(self, revoked=False):
        aawards = AttemptAward.objects.filter(
            attempt__attemptconfirmation__by=self.teacher,
            attempt__access_code=self.code.value,
            attempt__competitionquestionset=self.competition_questionset,
        )
        if not revoked:
            aawards = aawards.filter(revoked_by=None)
        return aawards.distinct()


class SchoolCategoryQuestionSets(models.Model):
    def __str__(self):
        return u"{} {}".format(self.competition, self.school_category)

    class Meta:
        unique_together = (("competition", "school_category"))

    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    questionsets = models.ManyToManyField(CompetitionQuestionSet)
    school_category = models.CharField(choices=SCHOOL_CATEGORIES, max_length=24)


class Award(models.Model):
    def __str__(self):
        return u"{} {} {} ({})".format(self.name, self.questionset.name,
                                       self.questionset.competition.slug, self.threshold)

    name = models.CharField(max_length=256)
    group_name = models.CharField(max_length=256)
    questionset = models.ForeignKey(CompetitionQuestionSet, on_delete=models.CASCADE)
    template = models.CharField(max_length=256, blank=True)
    icon = models.CharField(max_length=256, blank=True)
    threshold = models.FloatField(null=True, blank=True)
    min_threshold = models.FloatField()
    from_place = models.IntegerField(null=True, blank=True)
    to_place = models.IntegerField(null=True, blank=True)
    serial_prefix = models.CharField(max_length=256)
    replaces = models.ManyToManyField('Award', blank=True, related_name='replaced_by', symmetrical=False)


class AttemptAward(models.Model):
    def __str__(self):
        return u"{} {} {} {} {} ({})".format(self.attempt.competitor, self.award,
                                             self.attempt.score, self.serial, self.note, self.id)

    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE)
    note = models.CharField(max_length=1024, blank=True, default='')
    competitor_name = models.TextField(blank=True)
    school_name = models.TextField(blank=True)
    group_name = models.TextField(blank=True)
    revoked_by = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    serial = models.CharField(max_length=64, blank=True, default='', unique=True)
    files = models.ManyToManyField('AwardFile', blank=True)


class CompetitionRecognition(models.Model):
    def __str__(self):
        return self.template
    competition = models.ForeignKey(Competition, null=True, on_delete=models.CASCADE)
    template = models.CharField(max_length=256)
    serial_prefix = models.CharField(max_length=16)


class TeacherRecognition(models.Model):
    def __str__(self):
        return u"{} {}:{}".format(self.teacher, self.template, self.text)
    template = models.ForeignKey(CompetitionRecognition, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipient = models.TextField()
    text = models.TextField()
    serial = models.CharField(max_length=64, unique=True)
    note = models.CharField(max_length=1024,
                            blank=True, default='')
    revoked_by = models.ForeignKey(Profile, null=True,
                                   related_name='revoked_teacherrecognition_set',
                                   on_delete=models.CASCADE)
    files = models.ManyToManyField('AwardFile')


class AwardFile(models.Model):
    file = models.FileField()
    recipients = models.ManyToManyField(Profile, blank=True)


class SchoolCompetition(Competition):
    class Meta:
        proxy = True

    def questionsets_for_school_category(self, school_category):
        try:
            return SchoolCategoryQuestionSets.objects.get(
                    school_category=school_category, competition=self
                ).questionsets.all()
        except Exception as e:
            # TODO: handle exception
            pass
        return CompetitionQuestionSet.objects.none()

    def school_codes_create(self, school, teacher, access_code,
                            code_data=None):
        for cqs in self.questionsets_for_school_category(school_category=school.category):
            if code_data is not None:
                code_data['competition_questionset'] = cqs.slug_str()
            sc = self.school_code_create(school, teacher, access_code,
                                         competition_questionset=cqs,
                                         code_data=code_data)
            default_years = cqs.juniordefaultyear_set.filter(
                    school_category=school.category,
                )
            for dy in default_years:
                dy.create_year(sc)

    def school_code_create(self, school, teacher, access_code,
                           competition_questionset=None,
                           code_data=None):
        code = self.competitor_code_create(
            access_code, competition_questionset=competition_questionset, code_data=code_data)
        teacher.created_codes.add(code)
        sc = SchoolTeacherCode(teacher=teacher, school=school, code=code,
                               competition_questionset=competition_questionset)
        sc.save()
        return sc
