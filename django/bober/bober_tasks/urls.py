from django.conf.urls import url
from bober_tasks.views import *
from django.views.generic import RedirectView
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import reverse_lazy

urlpatterns = [
    # Index
    # url(r'^$', index, name="tasks_index"),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('tasks.list')),
        name="task_index"),
    # Translation
    url(r'^new/$', TaskCreate.as_view(), name="tasks.new"),
    url(r'^tasktranslation/(?P<pk>\d+)/clone$', tasktranslation_clone,
        name="tasktranslation_clone"),
    url(r'^tasktranslation/(?P<pk>\d+)/detail$',
        TaskTranslationDetail.as_view(),
        name="tasktranslation_detail"),
    url(r'^tasktranslation/(?P<pk>\d+)/resources/(?P<filename>\w.+)$',
        tasks_resource, name="tasktranslation.resource"),
    url(r'^tasktranslation/(?P<pk>\d+)/index.html$', tasktranslation_render,
        name="tasktranslation_render"),
    url(r'^tasktranslation/(?P<pk>\d+)/update$',
        TaskTranslationUpdate.as_view(), name="tasktranslation_update"),
    url(r'^tasktranslation/(?P<pk>\d+)/$', TaskTranslationDetail.as_view(),
        name="tasktranslation_detail"),
    url(r'^tasktranslation/(?P<pk>\d+)/preview$',
        TaskTranslationPreview.as_view(), name="tasktranslation_preview"),
    url(r'^tasktranslation/(?P<pk>\d+)/export$', export_to_simple_competition,
        name="export_to_simple_competition"),
    url(r'^tasktranslation/(?P<pk>\d+)/task.zip$', export_task_translation,
        name="export_zip"),
    url(r'^translation/save.?$', tasks_save_translation,
        name="tasks.translation_save"),
    url(r'^list/([a-z]*)$', tasks_list_language, name="tasks.list"),
    url(r'^list/$', tasks_list_language, name="tasks.list"),
    url(r'^history/(\d+)$', tasks_history, name="tasks.history"),
    # TODO: the code was badly broaken
    url(r'^new_from/(\d+)$', tasks_new_from, name="tasks.new_from"),
    url(r'^translate/(\d+)$', tasks_translate, name="tasks.translate"),
    url(r'^upload/(\d+)$', tasks_upload, name="tasks.upload"),
    # TODO: the code was badly broaken
    # url(r'^delete/(\d+)$', delete_task, name="tasks.delete"),
    url(r'^display/(\d+)/$', display_task, name="tasks.display"),
    url(r'^display/(\d+)/resources/(\w.+)$', tasks_resource,
        name="tasks.resource"),
    url(r'^export-multiple-tasks$', export_multiple_tasks,
        name="export_multiple_tasks"),

    # Task
    url(r'^task/(\d+)/$', task_detail, name="tasks.task"),
    url(r'^task/save$', save_task, name="tasks.task_save"),

    # Control Panel
    url(r'^control-panel/parameters?$', parameters,
        name="control_panel.parameters"),
    # Age groups
    url(r'^age-groups/?$', parameters, name="control_panel.age_groups"),
    url(r'^age-groups/(\d+)?$', edit_age_group,
        name="control_panel.edit_age_group"),
    url(r'^age-groups/new?$', new_age_group,
        name="control_panel.new_age_group"),
    url(r'^age-groups/delete/(\d+)?$', delete_age_group,
        name="control_panel.delete_age_group"),

    # Categories
    url(r'^categories/?$', parameters, name="control_panel.categories"),
    url(r'^categories/(\d+)?$', edit_category,
        name="control_panel.edit_category"),
    url(r'^categories/new?$', new_category, name="control_panel.new_category"),
    url(r'^categories/delete/(\d+)?$', delete_category,
        name="control_panel.delete_category"),

    # Difficulty levels
    url(r'^difficulty-levels/?$', parameters,
        name="control_panel.difficulty_levels"),
    url(r'^difficulty-levels/(\d+)?$', edit_difficulty,
        name="control_panel.edit_difficulty"),
    url(r'^difficulty-levels/new?$', new_difficulty,
        name="control_panel.new_difficulty"),
    url(r'^difficulty-levels/delete/(\d+)?$', delete_difficulty,
        name="control_panel.delete_difficulty"),
]

# urlpatterns += staticfiles_urlpatterns()
