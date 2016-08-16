from django.contrib import admin
from bober_tasks.models import *
from mce_filebrowser.admin import MCEFilebrowserAdmin

class TaskTranslationAdmin(MCEFilebrowserAdmin):
    pass

admin.site.register(AgeGroup)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(DifficultyLevel)
admin.site.register(Remark)
admin.site.register(Resources)
admin.site.register(Task)
admin.site.register(TaskTranslation, TaskTranslationAdmin)

