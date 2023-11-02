#from django.conf.urls import url
from django.urls import path
from bober_si.models import School
from bober_simple_competition.views import CompetitionDetail
from dal import autocomplete
from bober_si import views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    path(r'autocomplete/school/',
        autocomplete.Select2QuerySetView.as_view(model=School),
        name='school_autocomplete'),
    # 2. pick competition
    path(r'competition/<slug:slug>/overview',
        views.TeacherOverview.as_view(), name="teacher_overview"),
    path(r'competition/<slug:slug>/overviewx',
        views.TeacherOverview.as_view(template_name='bober_si/teacher_overviewx.html'), name="teacher_overviewx"),
    path(r'competition/<slug:slug>/award/<str:username>/recognitions/.*',
        views.mentor_recognition_pdf, name="mentor_recognition_pdf"),
    path(r'competition/<slug:slug>/award/<str:username>/by_school/<int:school_id>/<str:cqs_name>.pdf',
        views.school_awards_pdf, name="awards_school_pdf"),
    path(r'competition/<slug:slug>/award/<str:username>/by_school/<int:school_id>/<str:award_name>/<str:cqs_name>\.pdf',
        views.awards_school_type_pdf, name="awards_school_type_pdf"),
    path(r'competition/<slug:slug>/award/<str:username>/all/<str:cqs_name>\.pdf',
        views.all_awards_pdf, name="awards_all_pdf"),
    path(r'competition/<slug:slug>/award/<str:username>/by_type/<str:award_name>/<str:cqs_name>\.pdf',
        views.awards_type_pdf, name="awards_type_pdf"),
    path(r'competition/<slug:slug>/revalidate_awards/<int:profile_id>/<int:attempt_id>/',
        views.revalidate_awards, name="revalidate_awards"),
    path(r'results/<slug:slug>.xls',
        views.CompetitionXlsResults.as_view(), name="competition_results.xls"),
    path(r'results/<slug:slug>/<int:cqs_id>-<slug:cqs_slug>.xls',
        views.CompetitionXlsResults.as_view(), name="competitionquestionset_results.xls"),
    path(r'competition/<slug:slug>/profiles_by_school_category',
        views.ProfilesBySchoolCategory.as_view(), name="profiles_by_school_category"),
    path(r'competition/<slug:slug>/detail',
        CompetitionDetail.as_view(), name="competition_detail"),
    path(r'competition/<slug:slug>/school_codes_create',
        views.SchoolCodesCreate.as_view(), name="school_codes_create"),
    path(r'competition/<slug:slug>/teacher_registration',
        views.TeacherCodeRegistrationPasswordReset.as_view(), name="teacher_registration"),
]
