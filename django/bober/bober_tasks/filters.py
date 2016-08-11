import django_filters
from bober_tasks.models import *

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_type='startswith')

    class Meta:
        model = TaskTranslation
        fields = ['title', 'language_locale']
