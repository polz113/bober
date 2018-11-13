import django_filters
from bober_tasks.models import TaskTranslation


class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = TaskTranslation
        fields = ['title', 'language_locale']
