from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.event_details, name='event_details'),
)