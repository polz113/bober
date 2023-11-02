# from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from bober_simple_competition.models import Competition,\
    QuestionSet, Question
from dal import autocomplete
from bober_simple_competition import views


urlpatterns = [
    path(r'', views.index, name="simple_index"),
    path(r'', views.index, name="index"),
    # autocompletion links
    path(r'autocomplete/competition/',
        autocomplete.Select2QuerySetView.as_view(model=Competition),
        name='competition_autocomplete'),
    path(r'autocomplete/questionset/',
        autocomplete.Select2QuerySetView.as_view(model=QuestionSet),
        name='questionset_autocomplete'),
    path(r'autocomplete/question/',
        autocomplete.Select2QuerySetView.as_view(model=Question),
        name='question_autocomplete'),
    path(r'autocomplete/profile/',
        views.ProfileAutocomplete.as_view(),
        name='profile_autocomplete'),
    path(r'autocomplete/code/',
        views.CodeAutocomplete.as_view(),
        name='code_autocomplete'),
    # 1. login / enter access code
    path(r'access_code/<path:url_next>', views.access_code, name="access_code"),
    # 2. pick competition
    path(r'competition/id=', views.CompetitionList.as_view(),
        name="competition_list"),
    path(r'competition/', views.CompetitionList.as_view(),
        name="competition_list"),
    path(r'competition/id=<slug:pk>/detail',
        views.CompetitionDetail.as_view(), name="competition_detail"),
    path(r'competition/<slug:slug>/detail',
        views.CompetitionDetail.as_view(), name="competition_detail"),
    path(r'competition/<slug:slug>/overview',
        views.CompetitionDetail.as_view(), name="competition_overview"),
    path(r'competition/id=<int:pk>/update',
        views.CompetitionUpdate.as_view(), name="competition_update"),
    path(r'competition/<slug:slug>/update',
        views.CompetitionUpdate.as_view(), name="competition_update"),
    path(r'competition/id=create', views.CompetitionCreate.as_view(),
        name="competition_create"),
    #   2.1 teacher, admin (for this competition)
    #     2.1.1 create, list codes for competition
    path(r'competition/id=<int:id>/codes',
        views.competition_code_list, name="competition_code_list"),
    path(r'competition/<slug:slug>/codes',
        views.competition_code_list, name="competition_code_list"),
    path(r'competition/id=<int:id>/codes/<str:user_type>/create/',
        views.competition_code_create, name="competition_code_create"),
    path(r'competition/<slug:slug>/codes/<str:user_type>/create/',
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
    path(r'competition/id=<int:pk>/send_codes',
        views.send_codes, name="send_codes"),
    path(r'competition/<slug:slug>/send_codes',
        views.send_codes, name="send_codes"),
    #     2.1.3 view results
    path(r'competition/id=<int:pk>/attempts/',
        views.competition_attempt_list, name="competition_attempt_list"),
    path(r'competition/<slug:slug>/attempts/',
        views.competition_attempt_list, name="competition_attempt_list"),
    path(r'competition/id=<int:pk>/attempts/regrade',
        views.competition_attempt_list,
        {'regrade': True}, name="competition_attempt_list"),
    path(r'competition/<slug:slug>/attempts/regrade',
        views.competition_attempt_list,
        {'regrade': True}, name="competition_attempt_list"),
    #     2.1.4 mark attempts as invalid
    #           all attempts with codes created or distributed by
    #           the current user can be accessed
    path(r'competition/<slug:slug>/attempts/<int:competition_questonset_id>/<int:attempt_id>/invalidate',
        views.competition_attempt_list,
        {'regrade': True}, name="attempt_invalidate"),
    #     2.1.5
    path(r'competition/<slug:slug>/questionsets/use',
        views.use_questionsets, name="use_questionsets"),
    path(r'competition/<slug:slug>/questionsets/<int:competition_questionset_id>',
        views.use_questionsets, name="use_questionset"),
    #   2.2 competitor
    #     2.2.0 register as competitor using a code
    # compatibility redirect
    path(r'competitions/<slug:slug>/',
        RedirectView.as_view(pattern_name='competition_compete'),
        name="competition_compete_compat"),
    path(r'competition/<slug:slug>/',
        views.CompetitionCompete.as_view(), name="competition_compete"),
    path(r'competition/promoted/<slug:slug>/',
        views.CompetitionCompete.as_view(template_name="bober_simple_competition/index.html"),
        name="competition_compete_promoted"),
    path(r'competition/<slug:slug>/registration',
        views.CompetitionRegistration.as_view(), name="competition_registration"),
    path(r'compete/<int:competition_questionset_id>/access_code/<path:url_next>',
        views.competitionquestionset_access_code,
        name="competitionquestionset_access_code"),
    path(r'compete/<int:competition_questionset_id>/',
        views.QuestionSetCompete.as_view(), name="questionset_compete"),
    #     2.2.1 get question page
    path(r'compete/<int:competition_questionset_id>/resources/competition.html',
        views.competition_index, name="competition_index"),
    # 2.2.1.1 get question page as guest :: GUEST
    path(r'guest/compete/<int:competition_questionset_id>/',
        views.competition_guest, name="guest_compete"),
    path(r'guest/competition/<slug:slug>/',
        views.GuestCompetitionQuestionSetList.as_view(), name="guest_questionsets"),
    path(r'guest/competition/',
        views.GuestCompetitionList.as_view(), name="guest_competitions"),
    #     2.2.2 get question resources
    path(r'compete/<int:competition_questionset_id>/resources/<path:resource_path>',
        views.competition_resources, name="competition_resources"),
    # 2.2.3 get question data (existing answers, attempt_id, randomised_question map)
    path(r'compete/<int:competition_questionset_id>/data.json',
        views.competition_data, name="competition_data"),
    #     2.2.4 get remaining time
    path(r'compete/<int:competition_questionset_id>/attempts/<int:attempt_id>/time_remaining.json',
        views.time_remaining, name="time_remaining"),
    path(r'compete/<int:competition_questionset_id>/server_time.json',
        views.server_time, name="server_time"),
    #     2.2.5 submit answer
    path(r'compete/<int:competition_questionset_id>/attempts/<int:attempt_id>/submit.json',
        views.submit_answer, name="submit_answer"),
    #     2.2.6 finish competition
    path(r'compete/<int:competition_questionset_id>/attempts/<int:attempt_id>/finish.json',
        views.finish_competition, name="finish_competition"),
    #     2.2.7 view results
    path(r'compete/<int:competition_questionset_id>/attempts/regrade',
        views.competition_attempt_list, {'regrade': True},
        name="competition_attempt_list_regrade"),
    path(r'compete/<int:competition_questionset_id>/attempts/',
        views.competition_attempt_list, {'regrade': False},
        name="competition_attempt_list"),
    path(r'compete/<int:competition_questionset_id>/attempts/<int:attempt_id>/',
        views.attempt_results, name="attempt_results"),
    path(r'compete/<int:competition_questionset_id>/attempts/<int:attempt_id>/confirm',
        views.attempt_confirm, name="attempt_confirm"),
    path(r'compete/<int:competition_questionset_id>/attempts/<int:attempt_id>/unconfirm',
        views.attempt_unconfirm, name="attempt_unconfirm"),
    # 3. create registration codes
    path(r'registration_codes/', views.registration_codes,
        name="registration_codes"),
    # 5. edit user data
    # url(r'^users/', views.ProfileListView.as_view(), name="profile_list"),
    path(r'competitor/<int:pk>/update',
        views.CompetitorUpdateJson.as_view(), name='competitor_update'),
    path(r'profile/', views.ProfileTableView.as_view(), name="profile_list"),
    path(r'profile/<int:pk>/', views.ProfileDetail.as_view(),
        name="profile_detail"),
    #   5.1 merge users
    #    any users registered with codes created or distributed
    #    by the current user can be merged
    #   5.2 edit users
    #    the data for users registered with codes created or distributed
    #    by the current user can be edited
    path(r'profile/<int:pk>/update', views.ProfileUpdate.as_view(),
        name="profile_update"),
    path(r'profile/<int:pk>/merge', views.ProfileMerge.as_view(),
        name="profile_merge"),
    #   5.3 get certificates, other files
    path(r'profile/<int:pk>/files/<path:resource_path>',
        views.profile_files, name="profile_files"),
    path(r'profile/send-email', views.send_email, name="send_email"),
    path(r'send_to_mail', views.send_to_mail, name="send_to_mail"),
    # 6. import question(s)
    path(r'question/', views.QuestionList.as_view(), name="question_list"),
    path(r'question/<int:pk>/', views.QuestionDetail.as_view(),
        name="question_detail"),
    path(r'question/<int:pk>/', views.QuestionDetail.as_view(),
        name="question_index"),
    path(r'question/<int:pk>/resources/<path:resource_path>',
        views.question_resources, name="question_resource"),
    path(r'question/<int:pk>/solution/', views.QuestionSolution.as_view(),
        name="question_solution"),
    path(r'question/<int:pk>/solution/<path:resource_path',
        views.question_resources, name="question_solution_resource"),
    # 7. create questionset from questions
    path(r'questionset/id=', views.QuestionSetList.as_view(),
        name="questionset_list"),
    path(r'questionset/', views.QuestionSetList.as_view(),
        name="questionset_list"),
    path(r'questionset/id=create', views.QuestionSetCreate.as_view(),
        name="questionset_add"),
    path(r'questionset/id=create', views.QuestionSetCreate.as_view(),
        name="questionset_create"),
    path(r'questionset/', views.QuestionSetList.as_view(),
        name="questionset_id_list"),
    path(r'questionset/<slug:slug>/update',
        views.QuestionSetUpdate.as_view(),
        name="questionset_update"),
    path(r'questionset/id=<int:pk>/update',
        views.QuestionSetUpdate.as_view(),
        name="questionset_change"),
    path(r'questionset/id=<str:pk>/update', views.QuestionSetUpdate.as_view(),
        name="questionset_change"),
    path(r'questionset/id=<int:pk>/delete',
        views.QuestionSetDelete.as_view()),
    path(r'questionset/<slug:slug>/delete',
        views.QuestionSetDelete.as_view()),
    path(r'questionset/id=<int:pk>/', views.QuestionSetDetail.as_view(),
        name="questionset_detail"),
    path(r'questionset/<slug:slug>/', views.QuestionSetDetail.as_view(),
        name="questionset_detail"),
    #   all questions for competitions you have admin access to can be used
    # 8. create competition (from multiple questionsets)
    #   all questionsets for competitions you have admin access to can be used.
    #   Also, newly created questionsets can be used.
    # handling code formats
    path(r'code_format/', TemplateView.as_view(
            template_name="bober_simple_competition/codeformat_index.html"),
        name="code_format_index"),
    path(r'code_format/admin/', views.AdminCodeFormatList.as_view(),
        name="admin_code_format_list"),
    path(r'code_format/competitor/', views.CompetitorCodeFormatList.as_view(),
        name="competitor_code_format_list"),
    path(r'code_format/admin/<int:pk>', views.CodeFormatDetail.as_view(),
        name="admin_code_detail"),
    path(r'code_format/competitor/<int:pk>',
        views.CodeFormatDetail.as_view(),
        name="competitor_code_detail"),
    path(r'code_format/admin/create', views.AdminCodeFormatCreate.as_view(),
        name="admin_code_format_create"),
    path(r'code_format/competitor/create',
        views.CompetitorCodeFormatCreate.as_view(),
        name="competitor_code_format_create"),
    # shortcut for registering and competing immediately
]
