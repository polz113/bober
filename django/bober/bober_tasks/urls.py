#from django.conf.urls import url
from django.urls import path
from bober_tasks.views import *
from django.views.generic import RedirectView
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import reverse_lazy

urlpatterns = [
    # Index
    # url(r'^', index, name="tasks_index"),
    path(r'', RedirectView.as_view(url=reverse_lazy('tasks.list')),
        name="task_index"),
    # Translation
    path(r'new/', TaskCreate.as_view(), name="tasks.new"),
    path(r'tasktranslation/<int:pk>/clone', tasktranslation_clone,
        name="tasktranslation_clone"),
    path(r'tasktranslation/<int:pk>/detail',
        TaskTranslationDetail.as_view(),
        name="tasktranslation_detail"),
    path(r'tasktranslation/<int:pk>/resources/<path:filename>',
        tasks_resource, name="tasktranslation.resource"),
    path(r'tasktranslation/<int:pk>/index.html', tasktranslation_render,
        name="tasktranslation_render"),
    path(r'tasktranslation/<int:pk>/update',
        TaskTranslationUpdate.as_view(), name="tasktranslation_update"),
    path(r'tasktranslation/<int:pk>/', TaskTranslationDetail.as_view(),
        name="tasktranslation_detail"),
    path(r'tasktranslation/<int:pk>/preview',
        TaskTranslationPreview.as_view(), name="tasktranslation_preview"),
    path(r'tasktranslation/<int:pk>/export', export_to_simple_competition,
        name="export_to_simple_competition"),
    path(r'tasktranslation/<int:pk>/task.zip', export_task_translation,
        name="export_zip"),
    path(r'translation/save.?', tasks_save_translation,
        name="tasks.translation_save"),
    path(r'list/([a-z]*)', tasks_list_language, name="tasks.list"),
    path(r'list/', tasks_list_language, name="tasks.list"),
    path(r'history/(\d+)', tasks_history, name="tasks.history"),
    # TODO: the code was badly broaken
    path(r'new_from/(\d+)', tasks_new_from, name="tasks.new_from"),
    path(r'translate/(\d+)', tasks_translate, name="tasks.translate"),
    path(r'upload/(\d+)', tasks_upload, name="tasks.upload"),
    # TODO: the code was badly broaken
    # url(r'^delete/(\d+)', delete_task, name="tasks.delete"),
    path(r'display/(\d+)/', display_task, name="tasks.display"),
    path(r'display/(\d+)/resources/(\w.+)', tasks_resource,
        name="tasks.resource"),
    path(r'export-multiple-tasks', export_multiple_tasks,
        name="export_multiple_tasks"),

    # Task
    path(r'task/(\d+)/', task_detail, name="tasks.task"),
    path(r'task/save', save_task, name="tasks.task_save"),

    # Control Panel
    path(r'control-panel/parameters?', parameters,
        name="control_panel.parameters"),
    # Age groups
    path(r'age-groups/?', parameters, name="control_panel.age_groups"),
    path(r'age-groups/(\d+)?', edit_age_group,
        name="control_panel.edit_age_group"),
    path(r'age-groups/new?', new_age_group,
        name="control_panel.new_age_group"),
    path(r'age-groups/delete/(\d+)?', delete_age_group,
        name="control_panel.delete_age_group"),

    # Categories
    path(r'categories/?', parameters, name="control_panel.categories"),
    path(r'categories/(\d+)?', edit_category,
        name="control_panel.edit_category"),
    path(r'categories/new?', new_category, name="control_panel.new_category"),
    path(r'categories/delete/(\d+)?', delete_category,
        name="control_panel.delete_category"),

    # Difficulty levels
    path(r'difficulty-levels/?', parameters,
        name="control_panel.difficulty_levels"),
    path(r'difficulty-levels/(\d+)?', edit_difficulty,
        name="control_panel.edit_difficulty"),
    path(r'difficulty-levels/new?', new_difficulty,
        name="control_panel.new_difficulty"),
    path(r'difficulty-levels/delete/(\d+)?', delete_difficulty,
        name="control_panel.delete_difficulty"),
]

# urlpatterns += staticfiles_urlpatterns()
