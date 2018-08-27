from django.contrib import admin
from bober_simple_competition.models import CompetitionQuestionSet
from bober_si.models import School, Award, SchoolCategoryQuestionSets, AttemptAward,\
    SchoolTeacherCode, SchoolCompetition, CompetitionRecognition, TeacherRecognition

try:
    from import_export.admin import ImportExportActionModelAdmin  # @UnresolvedImport
    DefaultAdmin = ImportExportActionModelAdmin
except Exception:
    DefaultAdmin = admin.ModelAdmin


class SchoolTeacherCodeAdmin(DefaultAdmin):
    search_fields = [
        'code__value',
        'teacher__user__username',
        'teacher__user__first_name', 'teacher__user__last_name',
        'school__name'
    ]
    raw_id_fields = ['school', 'code', 'teacher']


class AttemptAwardAdmin(DefaultAdmin):
    search_fields = [
        "award__name",
        "competitor_name",
        "school_name",
        "group_name",
        "serial",
    ]
    raw_id_fields = ['attempt']


class SchoolAdmin(DefaultAdmin):
    model = School
    search_fields = ['name']


class AwardInline(admin.TabularInline):
    model = Award


class CompetitionQuestionSetInline(admin.TabularInline):
    model = CompetitionQuestionSet
    # form = CompetitionQuestionSetInlineAdminForm
    raw_id_fields = ('guest_code',)


class SchoolCategoryQuestionSetsInline(admin.TabularInline):
    model = SchoolCategoryQuestionSets

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "questionsets":
            if request._obj_ is not None:
                kwargs["queryset"] = CompetitionQuestionSet.objects.filter(
                        competition=request._obj_)
            else:
                kwargs["queryset"] = CompetitionQuestionSet.objects.none()
        return super(SchoolCategoryQuestionSetsInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class CompetitionAdmin(DefaultAdmin):
    inlines = [CompetitionQuestionSetInline, SchoolCategoryQuestionSetsInline]

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super(CompetitionAdmin, self).get_form(request, obj, **kwargs)


class CompetitionQuestionSetAdmin(DefaultAdmin):
    inlines = [AwardInline]
    model = CompetitionQuestionSet


# Register your models here.
admin.site.register(School, SchoolAdmin)
admin.site.register(Award, DefaultAdmin)
admin.site.register(AttemptAward, AttemptAwardAdmin)
admin.site.register(CompetitionQuestionSet, CompetitionQuestionSetAdmin)
admin.site.register(SchoolTeacherCode, SchoolTeacherCodeAdmin)
admin.site.register(SchoolCompetition, CompetitionAdmin)
admin.site.register(CompetitionRecognition, DefaultAdmin)
admin.site.register(TeacherRecognition, DefaultAdmin)
