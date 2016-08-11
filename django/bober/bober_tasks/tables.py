import django_tables2 as tables
from bober_tasks.models import *

class TaskTable(tables.Table):
    #title = tables.Column(verbose_name= 'Title' )
    body = tables.Column(verbose_name= 'Description')
    timestamp = tables.Column(verbose_name= 'Last Edit')
    title = tables.TemplateColumn('<a href="/tasks/tasktranslation/{{record.id}}/update">{{record.title}}</a>', verbose_name= 'Title')
    export = tables.TemplateColumn('<input type="checkbox" value="{{ record.pk }}" />', verbose_name="Export", orderable=False)
    class Meta:
        model = TaskTranslation
        fields = ('title', 'body', 'timestamp')
        attrs = {'class': 'taskTable table table-hover'}
