from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from bober_simple_competition.models import CompetitionQuestionSet,\
    Profile, Answer, GradedAnswer, AttemptConfirmation, Competition,\
    QuestionSet, ResourceCache, Competitor, Resource, Question, Attempt
from bober_simple_competition.forms import ProfileAdminForm,\
    AnswerAdminForm, AnswerInlineAdminForm


class CompetitionQuestionSetInline(admin.TabularInline):
    model = CompetitionQuestionSet
    raw_id_fields = ('guest_code',)


class CompetitionAdmin(admin.ModelAdmin):
    inlines = [CompetitionQuestionSetInline]


class QuestionSetAdmin(admin.ModelAdmin):
    filter_horizontal = ['questions']


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    fk_name = 'user'
    can_delete = False
    # filter_horizontal = ['created_codes', 'received_codes', 'used_codes',
    # 'questions', 'question_sets', 'created_question_sets']
    form = ProfileAdminForm


# Define a new User admin
class ProfileUserAdmin(UserAdmin):
    inlines = (ProfileInline, )


class AnswerInline(admin.TabularInline):
    model = Answer
    fk_name = 'attempt'
    can_delete = False
    form = AnswerInlineAdminForm


class GradedAnswerInline(admin.TabularInline):
    model = GradedAnswer
    can_delete = True
    raw_id_fields = ['attempt', 'question', 'answer']


class AttemptAdmin(admin.ModelAdmin):
    search_fields = (
        'id',
        'competitionquestionset__competition__slug',
        'competitionquestionset__name',
        'competitor__first_name', 'competitor__last_name',
        'access_code')
    raw_id_fields = ('competitor', 'invalidated_by')
    inlines = [GradedAnswerInline]

    def lookup_allowed(self, lookup, value):
        if lookup in self.search_fields:
            return True
        return super(AttemptAdmin, self).lookup_allowed(lookup, value)


class CompetitorAdmin(admin.ModelAdmin):
    raw_id_fields = ('profile',)


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ('attempt_id',)
    raw_id_fields = ('attempt',)
    form = AnswerAdminForm


class AttemptConfirmationAdmin(admin.ModelAdmin):
    search_fields = (
        'by__user__username', 'by__user__first_name', 'by__user__last_name',
        'attempt__id',
        'attempt__competitor__first_name', 'attempt__competitor__last_name')
    raw_id_fields = ('by', 'attempt')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, ProfileUserAdmin)

admin.site.register(AttemptConfirmation, AttemptConfirmationAdmin)
admin.site.register(Competitor, CompetitorAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(QuestionSet, QuestionSetAdmin)
admin.site.register(ResourceCache)
admin.site.register(Resource)
admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Attempt, AttemptAdmin)
