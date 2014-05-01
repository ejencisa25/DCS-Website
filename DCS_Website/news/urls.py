from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.news_details, name='news_details'),
)