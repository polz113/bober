from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles import views
from django.contrib import admin
import bober_paper_submissions.urls
import bober_simple_competition.urls
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bober.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='simple/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^school_mentor/', include(bober_paper_submissions.urls)),
    url(r'^simple/', include(bober_simple_competition.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
