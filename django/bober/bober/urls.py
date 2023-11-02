from django.conf.urls import include
from django.urls import path
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
    path(r'', RedirectView.as_view(url='simple/')),
    path(r'simple/', include(bober_si.urls)),
    path(r'simple/', include(bober_paper_submissions.urls)),
    path(r'simple/', include(bober_simple_competition.urls)),
    path(r'tasks/', include(bober_tasks.urls)),
    path(r'jsi18n/<path:packages>', JavaScriptCatalog.as_view(),
        kwargs={'domain': 'django'}, name='javascript-catalog'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    # path('', include('password_reset.urls')),
    path(r'admin/', admin.site.urls),
    path(r'impersonate/', include('impersonate.urls')),
    path(r'i18n/', include('django.conf.urls.i18n')),
    # url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path(r'static/<path:path>', views.serve),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
