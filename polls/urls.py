from django.conf.urls import patterns, urls, include
from polls import views


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)

url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),