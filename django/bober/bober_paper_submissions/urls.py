# from django.conf.urls import url
from django.urls import path
from bober_paper_submissions import views


urlpatterns = [
    # Examples:
    # url(r'^', 'bober.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path(r'competitions/<slug:slug>/junior_results/<int:pk>',
        views.JuniorResults.as_view(), name="junior_results"),
    path(r'competitions/<slug:slug>/junior_results',
        views.mentorship_list, name='mentorship_list'),
]
