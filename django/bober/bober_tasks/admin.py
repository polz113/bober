from django.contrib import admin
from bober_tasks.models import *
# from mce_filebrowser.admin import MCEFilebrowserAdmin

class AnswerInline(admin.TabularInline):
    model = Answer

# class TaskTranslationAdmin(MCEFilebrowserAdmin):
class TaskTranslationAdmin(admin.ModelAdmin):
    inlines = [ AnswerInline ]

admin.site.register(AgeGroup)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(DifficultyLevel)
admin.site.register(Remark)
admin.site.register(Resources)
admin.site.register(Task)
admin.site.register(TaskTranslation, TaskTranslationAdmin)

