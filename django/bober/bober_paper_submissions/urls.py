from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bober.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.school_mentor, name= "school_mentor"),
    url(r'^school/(?P<competition_category_school_mentor_id>\d+)/junior_results$', views.junior_results, name= "junior_results"),

)
