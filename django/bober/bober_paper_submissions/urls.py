from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from bober_competition.models import CompetitionCategory
import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bober.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.school_mentor, name= "school_mentor"),
    url(r'^competition_category/?$', ListView.as_view(model=CompetitionCategory), name="competition_category_list"),
    url(r'^competition_category/(?P<competition_category_id>\d+)/results.pickle$', views.competition_category_results_by_school, name= "competition_category_results_by_school"),
    url(r'^school/(?P<competition_category_school_mentor_id>\d+)/junior_results$', views.junior_results, name= "junior_results"),

)
