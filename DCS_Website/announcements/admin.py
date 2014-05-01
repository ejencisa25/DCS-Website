from django.contrib import admin
from announcements.models import Announcement

# Register your models here.
class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']

admin.site.register(Announcement, AnnouncementAdmin)