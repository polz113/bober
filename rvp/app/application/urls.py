from django.conf.urls import patterns, include, url
import views
from views import users, tasks, control_panel, api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Index
    url(r'^$', views.index, name="index"),

    # User
    url(r'^profile/?$', users.profile, name="users.profile"),
    url(r'^login/?$', users.login, name="users.login"),
    url(r'^register/?$', users.register, name="users.register"),
    url(r'^logout/?$', users.logout, name="users.logout"),
    url(r'^user/set_interface_lang/$', users.set_interface_lang, name="users.set_interface_lang"),
    url(r'^user/edit/?(\d+)$', users.edit_user, name="users.edit_user"),
    url(r'^user/delete/?(\d+)$', users.delete_user, name="users.delete_user"),
    url(r'^user/?(\d+)$', users.show_user, name="users.show_user"),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Translation
    url(r'^new/([a-z]+)?$', views.tasks.new, name="tasks.new"),
    url(r'^edit/(\d+)$', tasks.edit, name="tasks.edit"),
    url(r'^translation/save?$', tasks.save_translation, name="tasks.translation_save"),
    url(r'^list/([a-z]+)$', views.tasks.list_language, name="tasks.list"),
    url(r'^history/(\d+)$', tasks.history, name="tasks.history"),
    url(r'^new_from/(\d+)$', tasks.new_from, name="tasks.new_form"),
    url(r'^translate/(\d+)$', tasks.translate, name="tasks.translate"),
    url(r'^upload/(\d+)$', tasks.upload, name="tasks.upload"),
    url(r'^delete/(\d+)$', tasks.delete, name="tasks.delete"),
    url(r'^translation/save$', tasks.save_translation, name="tasks.translation_save"),
    url(r'^display/(\d+)/$', tasks.display, name="tasks.display"),
    url(r'^display/(\d+)/resources/(\w.+)$', tasks.resource, name="tasks.resource"),

    # Task
    url(r'^task/(\d+)/$', tasks.task, name="tasks.task"),
    url(r'^task/save$', tasks.save_task, name="tasks.task_save"),

    # Control Panel
    url(r'^control-panel/parameters?$', control_panel.parameters, name="control_panel.parameters"),
    url(r'^control-panel/users/?$', control_panel.users, name="control_panel.users"),

    # Age groups
    url(r'^age-groups/?$', control_panel.parameters, name="control_panel.age_groups"),
    url(r'^age-groups/(\d+)?$', control_panel.edit_age_group, name="control_panel.edit_age_group"),
    url(r'^age-groups/new?$', control_panel.new_age_group, name="control_panel.new_age_group"),
    url(r'^age-groups/delete/(\d+)?$', control_panel.delete_age_group, name="control_panel.delete_age_group"),

    # Languages
    url(r'^languages/?$', control_panel.parameters, name="control_panel.languages"),
    url(r'^languages/new/?$', control_panel.new_language, name="control_panel.new_language"),
    url(r'^languages/edit/([a-z]+)$', control_panel.edit_language, name="control_panel.edit_language"),
    url(r'^languages/delete/([a-z]+)?$', control_panel.delete_language, name="control_panel.delete_language"),

    # Categories
    url(r'^categories/?$', control_panel.parameters, name="control_panel.categories"),
    url(r'^categories/(\d+)?$', control_panel.edit_category, name="control_panel.edit_category"),
    url(r'^categories/new?$', control_panel.new_category, name="control_panel.new_category"),
    url(r'^categories/delete/(\d+)?$', control_panel.delete_category, name="control_panel.delete_category"),

    # Difficulty levels
    url(r'^difficulty-levels/?$', control_panel.parameters, name="control_panel.difficulty_levels"),
    url(r'^difficulty-levels/(\d+)?$', control_panel.edit_difficulty, name="control_panel.edit_difficulty"),
    url(r'^difficulty-levels/new?$', control_panel.new_difficulty, name="control_panel.new_difficulty"),
    url(r'^difficulty-levels/delete/(\d+)?$', control_panel.delete_difficulty, name="control_panel.delete_difficulty"),

    # International
    url(r'^i18n/', include('django.conf.urls.i18n'), name="i18n"),

    # API
    url(r'^export/task/(\d+)/([A-Za-z]+)$', views.export_task_language, name="api.export_task"), #vrne zadnji prevod za doloceno nalogo
    url(r'^export/task/(\d+)/([A-Za-z]+)/(\d+)$', views.export_task_language_version, name="api.export_task_version"), #vrne doloceno verzijo prevode za doloceno nalogo
    # Examples:
    # url(r'^$', 'application.views.home', name='home'),
    # url(r'^application/', include('application.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #(r'^ckeditor/', include('ckeditor.urls')),
    # Show static HTML
)

urlpatterns += staticfiles_urlpatterns()