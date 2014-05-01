from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DCS_Website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'DCS_Website.views.home', name='home'),
    url(r'^news/', include('news.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^announcements/', include('announcements.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
