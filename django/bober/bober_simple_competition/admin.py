from django.contrib import admin
from bober_simple_competition.models import *

# Register your models here.
class CompetitionQuestionSetInline(admin.TabularInline):
    model = CompetitionQuestionSet

class CompetitionAdmin(admin.ModelAdmin):
    inlines = [ CompetitionQuestionSetInline ]

admin.site.register(Competition, CompetitionAdmin)
admin.site.register(QuestionSet)
admin.site.register(ResourceCache)
admin.site.register(Resource)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Attempt)
admin.site.register(Profile)
