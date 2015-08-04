from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles import views
from django.contrib import admin
import django.contrib.auth.urls
import bober_paper_submissions.urls
import bober_simple_competition
import bober_simple_competition.urls
import bober_tasks
import bober_tasks.urls
from django.views.generic import RedirectView

admin.autodiscover()

js_info_dict = {
    'domain': 'django',
    'packages': ('bober_simple_competition',),
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bober.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='simple/')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('django.contrib.auth.urls')),
    url(r'^school_mentor/', include(bober_paper_submissions.urls)),
    url(r'^simple/', include(bober_simple_competition.urls)),
    url(r'^tasks/', include(bober_tasks.urls)),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog', 
        kwargs = {'domain': 'django'}),
    # url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
	url('^accounts/', include('django.contrib.auth.urls'))
)


if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
