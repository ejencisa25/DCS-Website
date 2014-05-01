from django.contrib import admin
from events.models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
	list_display = ('description', 'date')
	list_filter = ['date']
	search_fields = ['description']
	
admin.site.register(Event, EventAdmin)