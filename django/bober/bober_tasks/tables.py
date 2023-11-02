from django.utils.translation import gettext_lazy as _
import django_tables2 as tables
from bober_tasks.models import TaskTranslation


class TaskTable(tables.Table):
    body = tables.Column(verbose_name=_("Description"))
    timestamp = tables.Column(verbose_name=_('Last Edit'))
    title = tables.TemplateColumn('<a href="/tasks/tasktranslation/{{record.id}}/update">{{record.title}}</a>',
                                  verbose_name=_('Title'))
    export = tables.TemplateColumn('<input type="checkbox" name="taskValues" value="{{ record.pk }}" />',
                                   verbose_name=_('Export'), orderable=False)

    class Meta:
        model = TaskTranslation
        fields = ('title', 'body', 'timestamp')
        attrs = {'class': 'taskTable table table-hover'}
