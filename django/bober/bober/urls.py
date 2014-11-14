from django.conf.urls import patterns, include, url

from django.contrib import admin
import bober_paper_submissions.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bober.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^school_mentor/', include(bober_paper_submissions.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
