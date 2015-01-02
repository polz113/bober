from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from bober_simple_competition.models import *
import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="index"),
    # 1. login
    # 2. pick competition
    url(r'^competitions/$', views.CompetitionListView.as_view(), name="competition_list"),
    #   2.1 teacher, admin (for this competition)
    #     2.1.1 create, list codes for competition
    url(r'^competitions/(?P<competition_slug>[\w-]+)/codes$', views.competition_code_list, name="competition_code_list"),
    url(r'^competitions/(?P<competition_slug>[\w-]+)/codes/(?P<generator>[\w]+)/create/$', views.competition_code_create, name="competition_code_create"),
    #           codes can have the following permissions:
    #           1. can create admin codes for this competition
    #           2. can create teacher codes for this competition
    #           3. can create student codes for this competition
    #           4. can attempt competition
    #           5. can attempt competition before official start
    #           6. can view results before official end
    #           7. can use questionset to create new competitions
    #     2.1.2 distribute codes to registered and other users
    url(r'^competitions/(?P<competition_slug>[\w-]+)/send_codes$', views.send_codes, name="send_codes"),
    #     2.1.3 view results
    url(r'^competitions/(?P<competition_slug>[\w-]+)/attempts/$', views.competition_attempt_list, name="competition_attempt_list"),
    #     2.1.4 mark attempts as invalid
    #           all attempts with codes created or distributed by
    #           the current user can be accessed 
    url(r'^competitions/(?P<competition_slug>[\w-]+)/attempts/(?P<attempt_id>\d+)/disqualify$', views.disqualify_attempt, name="disqualify_attempt"),
    #   2.2 competitor
    #     2.2.0 register as competitor using a code
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/$', views.competition_registration, name="competition_registration"),
    #     2.2.1 get question page
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/resources/competition.html$', views.competition_index, name="competition_index"),
    #     2.2.2 get question resources
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/resources/(?P<resource_path>.*)', views.competition_resources, name="competition_resources"),
    #     2.2.3 get question data (existing answers, attempt_id, randomised_question map)
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/data.json$', views.competition_data, name="competition_data"),
    #     2.2.4 get remaining time
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/attempts/(?P<attempt_id>\d+)/time_remaining.json$', views.time_remaining, name="time_remaining"),
    #     2.2.5 submit answer
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/attempts/(?P<attempt_id>\d+)/submit.json$', views.submit_answer, name="submit_answer"),
    #     2.2.6 finish competition
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/attempts/(?P<attempt_id>\d+)/finish.json$', views.finish_competition, name="finish_competition"),
    #     2.2.7 view results
    url(r'^compete/(?P<competition_questionset_id>[\d]+)/attempts/(?P<attempt_id>\d+)/$', views.attempt_results, name="attempt_results"),
    # 3. create registration codes
    url(r'^registration_codes/$', views.registration_codes, name="registration_codes"),
    # 4. register as user
    url(r'^registration/$', views.user_registration, name="user_registration"),
    # 5. edit user data
    url(r'^users/$', views.user_list, name="user_list"),
    #   5.1 merge users
    #    any users registered with codes created or distributed
    #    by the current user can be merged
    url(r'^user_merge/$', views.user_merge, name="user_merge"),
    #   5.2 edit users
    #    the data for users registered with codes created or distributed
    #    by the current user can be edited
    url(r'^users/(?P<user_id>\d+)/$', views.user_edit, name="user_edit"),
    #   5.3 get certificates, other files
    url(r'^users/(?P<user_id>\d+)/files$', views.user_files, name="user_files"),
    # 6. import question(s)
    url(r'^question_import/$', views.question_import, name="question_import"),
    # 7. create questionset from questions
    url(r'^questionset_create/$', views.questionset_create, name="questionset_create"),
    #   all questions for competitions you have admin access to can be used
    # 8. create competition (from multiple questionsets)
    #   all questionsets for competitions you have admin access to can be used.
    #   Also, newly created questionsets can be used.
    url(r'^competition_create/$', views.competition_create, name="competition_create"),
    # shortcut for registering and competing immediately 
    url(r'^immediate_competition/$', views.immediate_competition, name="immediate_competition"),
)
