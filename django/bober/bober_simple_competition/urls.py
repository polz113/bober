from django.conf.urls import include, url
from django.views.generic import ListView, TemplateView
from django.views.generic.base import RedirectView
from bober_simple_competition.models import Competition,\
    QuestionSet, Question
from dal import autocomplete
from bober_simple_competition import views


urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="simple_index"),
    url(r'^$', views.index, name="index"),
    # autocompletion links
    url(r'autocomplete/competition/$',
        autocomplete.Select2QuerySetView.as_view(model=Competition),
        name='competition_autocomplete'),
    url(r'autocomplete/questionset/$',
        autocomplete.Select2QuerySetView.as_view(model=QuestionSet),
        name='questionset_autocomplete'),
    url(r'autocomplete/question/$',
        autocomplete.Select2QuerySetView.as_view(model=Question),
        name='question_autocomplete'),
    url(r'autocomplete/profile/$',
        views.ProfileAutocomplete.as_view(),
        name='profile_autocomplete'),
    url(r'autocomplete/code/$',
        views.CodeAutocomplete.as_view(),
        name='code_autocomplete'),
    # 1. login / enter access code
    url(r'^access_code/*(?P<next>.*)$', views.access_code, name="access_code"),
    # 2. pick competition
    url(r'^competition/id=$', views.CompetitionList.as_view(), name="competition_list"),
    url(r'^competition/$', views.CompetitionList.as_view(), name="competition_list"),
    url(r'^competition/id=(?P<pk>[\w\-_]+)/detail$',
        views.CompetitionDetail.as_view(), name="competition_detail"),
    url(r'^competition/(?P<slug>[\w\-_]+)/detail$',
        views.CompetitionDetail.as_view(), name="competition_detail"),
    url(r'^competition/(?P<slug>[\w\-_]+)/overview$',
        views.CompetitionDetail.as_view(), name="competition_overview"),
    url(r'^competition/id=(?P<pk>\d+)/update$',
        views.CompetitionUpdate.as_view(), name="competition_update"),
    url(r'^competition/(?P<slug>[\w\-_]+)/update$',
        views.CompetitionUpdate.as_view(), name="competition_update"),
    url(r'^competition/id=create$', views.CompetitionCreate.as_view(),
        name="competition_create"),
    #   2.1 teacher, admin (for this competition)
    #     2.1.1 create, list codes for competition
    url(r'^competition/id=(?P<id>\d+)/codes$',
        views.competition_code_list, name="competition_code_list"),
    url(r'^competition/(?P<slug>[\w\-_]+)/codes$',
        views.competition_code_list, name="competition_code_list"),
    url(r'^competition/id=(?P<id>\d+)/codes/(?P<user_type>[\w]+)/create/$',
        views.competition_code_create, name="competition_code_create"),
    url(r'^competition/(?P<slug>[\w\-_]+)/codes/(?P<user_type>[\w]+)/create/$',
        views.competition_code_create, name="competition_code_create"),
    #           codes can have the following permissions:
    #           1. can create admin codes for this competition
    #           2. can create teacher codes for this competition
    #           3. can create student codes for this competition
    #           4. can attempt competition
    #           5. can attempt competition before official start
    #           6. can view results before official end
    #           7. can use questionset to create new competitions
    #     2.1.2 distribute codes to registered and other users
    url(r'^competition/id=(?P<pk>\d+)/send_codes$',
        views.send_codes, name="send_codes"),
    url(r'^competition/(?P<slug>[\w\-_]+)/send_codes$',
        views.send_codes, name="send_codes"),
    #     2.1.3 view results
    url(r'^competition/id=(?P<pk>\d+)/attempts/$',
        views.competition_attempt_list, name="competition_attempt_list"),
    url(r'^competition/(?P<slug>[\w\-_]+)/attempts/$',
        views.competition_attempt_list, name="competition_attempt_list"),
    url(r'^competition/id=(?P<pk>\d+)/attempts/regrade$',
        views.competition_attempt_list, {'regrade':True}, name="competition_attempt_list"),
    url(r'^competition/(?P<slug>[\w\-_]+)/attempts/regrade$',
        views.competition_attempt_list, {'regrade':True}, name="competition_attempt_list"),
    #     2.1.4 mark attempts as invalid
    #           all attempts with codes created or distributed by
    #           the current user can be accessed
    url(r'^competition/(?P<slug>[\w\-_]+)/attempts/(?P<competition_questonset_id>\d+)/(?P<attempt_id>\d+)/invalidate$',
        views.competition_attempt_list, {'regrade':True}, name="attempt_invalidate"),
    #     2.1.5
    #url(r'^competition/(?P<slug>[\w\-_]+)/questionsets/use$',
    #    views.use_questionsets, name="use_questionsets"),
    url(r'^competition/(?P<slug>[\w\-_]+)/questionsets/use$',
        views.use_questionsets, name="use_questionsets"),
    url(r'^competition/(?P<slug>[\w\-_]+)/questionsets/(?P<competition_questionset_id>[\d]+)$',
        views.use_questionsets, name="use_questionset"),
    #   2.2 competitor
    #     2.2.0 register as competitor using a code
    # compatibility redirect
    url(r'^competitions/(?P<slug>[\w\-_]+)/$',
        RedirectView.as_view(pattern_name='competition_compete'), 
        name="competition_compete_compat"),
    url(r'^competition/(?P<slug>[\w\-_]+)/$',
        views.CompetitionCompete.as_view(), name="competition_compete"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/registration$',
        views.CompetitionRegistration.as_view(), name="competition_registration"),
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/access_code/(?P<next>.*)$',
        views.competitionquestionset_access_code,
        name="competitionquestionset_access_code"),
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/$',
        views.QuestionSetCompete.as_view(), name="questionset_compete"),
    #     2.2.1 get question page
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/resources/competition.html$',
        views.competition_index, name="competition_index"),
	#     2.2.1.1 get question page as guest :: GUEST
    url(r'^guest/(?P<competition_questionset_id>[\d]+)/$',
        views.competition_guest, name="competition_guest"),
    #     2.2.2 get question resources
    url(r'^compete/(?P<competition_questionset_id>\d+)/resources/(?P<resource_path>.*)',
        views.competition_resources, name="competition_resources"),
    #     2.2.3 get question data (existing answers, attempt_id, randomised_question map)
    url(r'^compete/(?P<competition_questionset_id>\d+)/data.json$',
        views.competition_data, name="competition_data"),
    #     2.2.4 get remaining time
    url(r'^compete/(?P<competition_questionset_id>\d+)/attempts/(?P<attempt_id>\d+)/time_remaining.json$',
        views.time_remaining, name="time_remaining"),
    url(r'^compete/(?P<competition_questionset_id>\d+)/server_time.json$',
        views.server_time, name="server_time"),
    #     2.2.5 submit answer
    url(r'^compete/(?P<competition_questionset_id>\d+)/attempts/(?P<attempt_id>\d+)/submit.json$',
        views.submit_answer, name="submit_answer"),
    #     2.2.6 finish competition
    url(r'^compete/(?P<competition_questionset_id>\d+)/attempts/(?P<attempt_id>\d+)/finish.json$',
        views.finish_competition, name="finish_competition"),
    #     2.2.7 view results
    url(r'^compete/(?P<competition_questionset_id>\d+)/attempts/regrade$',
        views.competition_attempt_list, {'regrade':True}, name="competition_attempt_list_regrade"),
    url(r'^compete/(?P<competition_questionset_id>\d+)/attempts/$',
        views.competition_attempt_list, {'regrade':False}, name="competition_attempt_list"),
    url(r'^compete/(?P<competition_questionset_id>\d+)/attempts/(?P<attempt_id>\d+)/$',
        views.attempt_results, name="attempt_results"),
    url(r'^compete/(?P<competition_questionset_id>\d+)/attempts/(?P<attempt_id>\d+)/confirm$',
        views.attempt_confirm, name="attempt_confirm"),
    url(r'^compete/(?P<competition_questionset_id>\d+)/attempts/(?P<attempt_id>\d+)/unconfirm$',
        views.attempt_unconfirm, name="attempt_unconfirm"),
    # 3. create registration codes
    url(r'^registration_codes/$', views.registration_codes, name="registration_codes"),
    # 5. edit user data
    # url(r'^users/$', views.ProfileListView.as_view(), name="profile_list"),
    url(r'^competitor/(?P<pk>\d+)/update', views.CompetitorUpdateJson.as_view(), name='competitor_update'),
    url(r'^profile/$', views.ProfileTableView.as_view(), name="profile_list"),
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileDetail.as_view(), name="profile_detail"),
    #   5.1 merge users
    #    any users registered with codes created or distributed
    #    by the current user can be merged
    #   5.2 edit users
    #    the data for users registered with codes created or distributed
    #    by the current user can be edited
    url(r'^profile/(?P<pk>\d+)/update$', views.ProfileUpdate.as_view(), name="profile_update"),
    url(r'^profile/(?P<pk>\d+)/merge$', views.ProfileMerge.as_view(), name="profile_merge"),
    #   5.3 get certificates, other files
    url(r'^profile/(?P<pk>\d+)/files/(?P<resource_path>)$', views.profile_files, name="profile_files"),
    url(r'^profile/send-email$', views.send_email, name="send_email"),
    url(r'^send_to_mail$', views.send_to_mail, name="send_to_mail"),
    # 6. import question(s)
    url(r'^question/$', views.QuestionList.as_view(), name="question_list"),
    # TODO: figure out a way to have safe checkers
    #url(r'^question/import$', views.QuestionImport.as_view(), name="question_import"),
    #url(r'^question/create$', views.QuestionCreate.as_view(), name="question_create"),
    #url(r'^question/(?P<pk>\d+)/update$', views.QuestionUpdate.as_view(), name="question_update"),
    url(r'^question/(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name="question_detail"),
    url(r'^question/(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name="question_index"),
    # url(r'^question/(?P<pk>\d+)/resources/$', views.QuestionDetail.as_view(), name="question_text"),
    url(r'^question/(?P<pk>\d+)/resources/(?P<resource_path>.*)$', views.question_resources, name="question_resource"),
    url(r'^question/(?P<pk>\d+)/solution/$', views.QuestionSolution.as_view(), name="question_solution"),
    url(r'^question/(?P<pk>\d+)/solution/(?P<resource_path>.*)$', views.question_resources, name="question_solution_resource"),
    # 7. create questionset from questions
    url(r'^questionset/id=$', views.QuestionSetList.as_view(), name="questionset_list"),
    url(r'^questionset/$', views.QuestionSetList.as_view(), name="questionset_list"),
    url(r'^questionset/id=create', views.QuestionSetCreate.as_view(),
        name="questionset_add"),
    url(r'^questionset/id=create', views.QuestionSetCreate.as_view(),
        name="questionset_create"),
    url(r'^questionset/$', views.QuestionSetList.as_view(), name="questionset_id_list"),
    url(r'^questionset/(?P<slug>[\w\-_]+)/update$', views.QuestionSetUpdate.as_view(),
        name="questionset_update"),
    url(r'^questionset/id=(?P<pk>.*)/update$', views.QuestionSetUpdate.as_view(),
        name="questionset_change"),
    url(r'^questionset/id=(?P<pk>.*)/update$', views.QuestionSetUpdate.as_view(),
        name="questionset_change"),
    url(r'^questionset/id=(?P<pk>\d+)/delete$', views.QuestionSetDelete.as_view()),
    url(r'^questionset/(?P<slug>[\w\-_]+)/delete$', views.QuestionSetDelete.as_view()),
    url(r'^questionset/id=(?P<pk>\d+)/$', views.QuestionSetDetail.as_view(),
        name="questionset_detail"),
    url(r'^questionset/(?P<slug>[\w\-_]+)/$', views.QuestionSetDetail.as_view(),
        name="questionset_detail"),
    #   all questions for competitions you have admin access to can be used
    # 8. create competition (from multiple questionsets)
    #   all questionsets for competitions you have admin access to can be used.
    #   Also, newly created questionsets can be used.
    # handling code formats
    url(r'^code_format/$', TemplateView.as_view(
            template_name="bober_simple_competition/codeformat_index.html"),
        name="code_format_index"),
    url(r'^code_format/admin/$', views.AdminCodeFormatList.as_view(),
        name="admin_code_format_list"),
    url(r'^code_format/competitor/$', views.CompetitorCodeFormatList.as_view(),
        name="competitor_code_format_list"),
    url(r'^code_format/admin/(?P<pk>\d+)$', views.CodeFormatDetail.as_view(),
        name="admin_code_detail"),
    url(r'^code_format/competitor/(?P<pk>\d+)$', views.CodeFormatDetail.as_view(),
        name="competitor_code_detail"),
    url(r'^code_format/admin/create$', views.AdminCodeFormatCreate.as_view(),
        name="admin_code_format_create"),
    url(r'^code_format/competitor/create$', views.CompetitorCodeFormatCreate.as_view(),
        name="competitor_code_format_create"),
    # shortcut for registering and competing immediately
]
