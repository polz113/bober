from django.conf.urls import url
from bober_paper_submissions import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'bober.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^competitions/(?P<slug>[\w\-_]+)/junior_results/(?P<pk>\d+)$',
        views.JuniorResults.as_view(), name="junior_results"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/junior_results',
        views.mentorship_list, name='mentorship_list'),
]
