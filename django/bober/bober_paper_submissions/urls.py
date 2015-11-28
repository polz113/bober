from django.conf.urls import patterns, include, url
from django.views.generic import ListView
import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bober.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^competitions/(?P<slug>[\w\-_]+)/junior_results/(?P<pk>\d+)$', views.JuniorResults.as_view(), name= "junior_results"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/junior_results', views.mentorship_list, name='mentorship_list'),
    url(r'^competitions/(?P<slug>[\w\-_]+)/junior_awards/(?P<school_id>\d+)/(?P<year_name>.*).pdf$', views.junior_award_pdf, name='junior_award_pdf'),
)
