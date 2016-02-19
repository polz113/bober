from django.conf.urls import include, url
from django.views.generic import ListView
from bober_simple_competition.models import *
from bober_simple_competition.views import CompetitionDetail
import views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # 2. pick competition
    url(r'^competitions/(?P<slug>[\w\-_]+)/overview$', 
        views.TeacherOverview.as_view(), name="teacher_overview"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/overviewx$', 
        views.TeacherOverview.as_view(template_name='bober_si/teacher_overviewx.html'), name="teacher_overviewx"),
    url(r'^competitions/(?P<username>[^/]*)/potrdilo.pdf$', 
        views.mentor_certificate_pdf, name="mentor_certificate_pdf"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/award/(?P<username>[^/]*)/(?P<school_id>\d+)/(?P<cqs_name>.*).pdf$', 
        views.school_awards_pdf, name="school_awards_pdf"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/award/(?P<username>[^/]*)/(?P<cqs_name>.*).pdf$', 
        views.all_awards_pdf, name="all_awards_pdf"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/revalidate_awards/(?P<profile_id>\d+)/(?P<attempt_id>\d+)/$', 
        views.revalidate_awards, name="revalidate_awards"),
    url(r'^results/(?P<slug>[\w\-_]+)\.xls$',
        views.CompetitionXlsResults.as_view(), name="competition_results.xls"),
    url(r'^results/(?P<slug>[\w\-_]+)/(?P<cqs_id>\d+)-(?P<cqs_slug>.*)\.xls$', 
        views.CompetitionXlsResults.as_view(), name="competitionquestionset_results.xls"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/profiles_by_school_category$', 
        views.ProfilesBySchoolCategory.as_view(), name="profiles_by_school_category"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/detail$', 
        CompetitionDetail.as_view(), name="competition_detail"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/school_codes_create$', 
        views.SchoolCodesCreate.as_view(), name="school_codes_create"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/teacher_registration$', 
        views.TeacherCodeRegistrationPasswordReset.as_view(), name="teacher_registration"),
    #url(r'^competitions/(?P<slug>[\w\-_]+)/$', 
    #    views.TeacherOverview.as_view(), name="teacher_overview"),
]
