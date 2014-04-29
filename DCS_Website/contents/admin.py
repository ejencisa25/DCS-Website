from django.contrib import admin
from contents.models import Announcement, Event, NewsArticle

# Register your models here.
class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']

class EventAdmin(admin.ModelAdmin):
	list_display = ('description', 'date')
	list_filter = ['date']
	search_fields = ['description']

class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(NewsArticle, NewsAdmin)