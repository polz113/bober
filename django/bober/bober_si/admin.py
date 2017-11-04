from django.contrib import admin
from bober_si.models import *
from bober_simple_competition.models import CompetitionQuestionSet
from import_export.admin import ImportExportActionModelAdmin


class AwardInline(admin.TabularInline):
    model = Award


class CompetitionQuestionSetInline(admin.TabularInline):
    model = CompetitionQuestionSet
    # inlines = [ AwardInline ]


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

class CompetitionAdmin(admin.ModelAdmin):
    inlines = [ CompetitionQuestionSetInline, SchoolCategoryQuestionSetsInline ]
    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super(CompetitionAdmin, self).get_form(request, obj, **kwargs)

class CompetitionQuestionSetAdmin(admin.ModelAdmin):
    inlines = [ AwardInline ]
    model = CompetitionQuestionSet

class SchoolAdmin(ImportExportActionModelAdmin):
    model = School
    search_fields = ['name']

# Register your models here.
admin.site.register(School, SchoolAdmin)
admin.site.register(Award)
admin.site.register(AttemptAward)
admin.site.register(CompetitionQuestionSet, CompetitionQuestionSetAdmin)
admin.site.register(SchoolTeacherCode)
admin.site.register(SchoolCompetition, CompetitionAdmin)
admin.site.register(CompetitionRecognition)
admin.site.register(TeacherRecognition)
