from django.contrib import admin
from bober_paper_submissions.models import *

class JuniorAttemptInline(admin.TabularInline):
    model = JuniorAttempt

class JuniorYearAdmin(admin.ModelAdmin):
    model = JuniorYear
    inlines = [JuniorAttemptInline,]

class JuniorYearInline(admin.TabularInline):
    model = JuniorYear

class JuniorMentorshipAdmin(admin.ModelAdmin):
    inlines = [ JuniorYearInline ]
    search_fields = ['teacher__user__username', 'school__name']

# Register your models here.
admin.site.register(JuniorMentorship, JuniorMentorshipAdmin)
admin.site.register(JuniorDefaultYear)
admin.site.register(JuniorYear, JuniorYearAdmin)
