from django.conf.urls import patterns, url

from announcements import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.announcement_details, name='announcement_details'),
)