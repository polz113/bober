from django.contrib import admin
from bober_si.models import *
from bober_simple_competition.models import CompetitionQuestionSet

class CompetitionQuestionSetInline(admin.TabularInline):
    model = CompetitionQuestionSet

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

# Register your models here.
admin.site.register(School)
admin.site.register(SchoolTeacherCode)
admin.site.register(SchoolCompetition, CompetitionAdmin)
