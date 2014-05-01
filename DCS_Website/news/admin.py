from django.contrib import admin
from news.models import NewsArticle

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']
	
admin.site.register(NewsArticle, NewsAdmin)