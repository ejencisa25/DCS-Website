from django.shortcuts import render
from news.models import NewsArticle

# Create your views here.
def news_details(request, pk):
	news_article = NewsArticle.objects.get(id=pk)
	context = {'news_article' : news_article}
	return render(request, 'news/news.html', context)