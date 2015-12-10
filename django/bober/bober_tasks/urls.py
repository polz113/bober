from django.conf.urls import patterns, include, url
from bober_tasks.views import *
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    # Index
    # url(r'^$', index, name="tasks_index"),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('tasks.list')), name="task_index"),
    # Translation
    url(r'^new/$', TaskCreate.as_view(), name="tasks.new"),
    # url(r'^edit/(\d+)/resources/(\w.+)$', tasks_resource, name="tasks.resource"),
    # url(r'^edit/(\d+)/$', edit_task, name="tasks.edit"),
    url(r'^tasktranslation/(?P<pk>\d+)/clone$', tasktranslation_clone, name="tasktranslation_clone"),
    url(r'^tasktranslation/(?P<pk>\d+)/detail$', TaskTranslationDetail.as_view(), name="tasktranslation_detail"),
    url(r'^tasktranslation/(\d+)/resources/(\w.+)$', tasks_resource, name="tasktranslation.resource"),
    url(r'^tasktranslation/(?P<pk>\d+)/index.html$', tasktranslation_render, name="tasktranslation_render"),
    url(r'^tasktranslation/(?P<pk>\d+)/update$', TaskTranslationUpdate.as_view(), name="tasktranslation_update"),
    url(r'^tasktranslation/(?P<pk>\d+)/detail$', TaskTranslationDetail.as_view(), name="tasktranslation_detail"),
    url(r'^tasktranslation/(?P<pk>\d+)/$', TaskTranslationPreview.as_view(), name="tasktranslation_preview"),
    url(r'^tasktranslation/(?P<pk>\d+)/export$', export_to_simple_competition, name="export_to_simple_competition"),
    url(r'^translation/save.?$', tasks_save_translation, name="tasks.translation_save"),
    url(r'^list/([a-z]*)$', tasks_list_language, name="tasks.list"),
    url(r'^list/$', tasks_list_language, name="tasks.list"),
    url(r'^history/(\d+)$', tasks_history, name="tasks.history"),
    url(r'^new_from/(\d+)$', tasks_new_from, name="tasks.new_form"),
    url(r'^translate/(\d+)$', tasks_translate, name="tasks.translate"),
    url(r'^upload/(\d+)$', tasks_upload, name="tasks.upload"),
    url(r'^delete/(\d+)$', delete_task, name="tasks.delete"),
    url(r'^display/(\d+)/$', display_task, name="tasks.display"),
    # url(r'^display/(\d+)/$', TaskDetail., name="tasks.display"),
    url(r'^display/(\d+)/resources/(\w.+)$', tasks_resource, name="tasks.resource"),

    # Task
    url(r'^task/(\d+)/$', task_detail, name="tasks.task"),
    url(r'^task/save$', save_task, name="tasks.task_save"),

    # Control Panel
    url(r'^control-panel/parameters?$', parameters, name="control_panel.parameters"),
    # Age groups
    url(r'^age-groups/?$', parameters, name="control_panel.age_groups"),
    url(r'^age-groups/(\d+)?$', edit_age_group, name="control_panel.edit_age_group"),
    url(r'^age-groups/new?$', new_age_group, name="control_panel.new_age_group"),
    url(r'^age-groups/delete/(\d+)?$', delete_age_group, name="control_panel.delete_age_group"),

    # Categories
    url(r'^categories/?$', parameters, name="control_panel.categories"),
    url(r'^categories/(\d+)?$', edit_category, name="control_panel.edit_category"),
    url(r'^categories/new?$', new_category, name="control_panel.new_category"),
    url(r'^categories/delete/(\d+)?$', delete_category, name="control_panel.delete_category"),

    # Difficulty levels
    url(r'^difficulty-levels/?$', parameters, name="control_panel.difficulty_levels"),
    url(r'^difficulty-levels/(\d+)?$', edit_difficulty, name="control_panel.edit_difficulty"),
    url(r'^difficulty-levels/new?$', new_difficulty, name="control_panel.new_difficulty"),
    url(r'^difficulty-levels/delete/(\d+)?$', delete_difficulty, name="control_panel.delete_difficulty"),

    # International
    # url(r'^i18n/', include('django.conf.urls.i18n'), name="i18n"),

    # API
    url(r'^export/task/(\d+)/([A-Za-z]+)$', export_task_language, name="api.export_task"), #vrne zadnji prevod za doloceno nalogo
    url(r'^export/task/(\d+)/([A-Za-z]+)/(\d+)$', export_task_language_version, name="api.export_task_version"), #vrne doloceno verzijo prevode za doloceno nalogo
    # Examples:
    # url(r'^$', 'application.views.home', name='home'),
    # url(r'^application/', include('application.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #(r'^ckeditor/', include('ckeditor.urls')),
    # Show static HTML
]

urlpatterns += staticfiles_urlpatterns()
