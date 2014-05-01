from django.db import models

# Create your models here.
class NewsArticle(models.Model):
	pub_date = models.DateTimeField('Date Published')
	title = models.CharField(max_length=100)
	body = models.TextField(max_length=1000)
	def __str__(self):  # Python 3: def __str__(self):
		return self.title