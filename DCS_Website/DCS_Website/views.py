from django.shortcuts import render
from django.http import HttpResponse
from news.models import NewsArticle
from events.models import Event
from announcements.models import Announcement

# Create your views here.
def home(request):
    latest_news_article_list = NewsArticle.objects.order_by('-pub_date')[:3]
    latest_event_list = Event.objects.order_by('-date')[:3]
    latest_announcement_list = Announcement.objects.order_by('-pub_date')[:3]
    context = {'latest_news_article_list' : latest_news_article_list,
    			'latest_event_list' : latest_event_list,
    			'latest_announcement_list' : latest_announcement_list}
    return render(request, 'home/home.html', context)