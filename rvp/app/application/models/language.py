from django.db import models
from django.db.models import Max
from task_translation import TaskTranslation

class Language(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    value = models.CharField(max_length=45)
    def current_tasks(self):
        list  = []
        #tasks = self.tasktranslation_set.order_by('-version').values('task').annotate(max_version=Max('version')).values('id', 'title')
        tasks = TaskTranslation.objects.filter(
            language_locale=self.id
            ).values(
                'task'
                ).annotate(
                version=Max('version')
            )
        for task in tasks:
            list.append(self.tasktranslation_set.get(version = task['version'], task_id = task['task']))
        return list



    # For syncdb to work
    class Meta:
        app_label = 'application'