from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles import views
from django.views.i18n import JavaScriptCatalog
from django.contrib import admin
import bober_paper_submissions.urls
import bober_simple_competition.urls
import bober_tasks.urls
import bober_si.urls
from django.views.generic import RedirectView

# autocomplete_light.registry.autodiscover()
admin.autodiscover()

js_info_dict = {
    'domain': 'django',
    'packages': ('bober_simple_competition',),
}

urlpatterns = [
    # Examples:
    # url(r'^$', 'bober.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='simple/')),
    url(r'^simple/', include(bober_si.urls)),
    url(r'^simple/', include(bober_paper_submissions.urls)),
    url(r'^simple/', include(bober_simple_competition.urls)),
    url(r'^tasks/', include(bober_tasks.urls)),
    url(r'^jsi18n/(?P<packages>\S+?)/$', JavaScriptCatalog.as_view(),
        kwargs={'domain': 'django'}, name='javascript-catalog'),
    url('^accounts/', include('django.contrib.auth.urls')),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('password_reset.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^impersonate/', include('impersonate.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
