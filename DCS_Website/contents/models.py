from django.db import models

# Create your models here.
class Announcement(models.Model):
	pub_date = models.DateTimeField('Date Published')
	title = models.CharField(max_length=50)
	body = models.CharField(max_length=100)
	def __str__(self):  # Python 3: def __str__(self):
		return self.title

class Event(models.Model):
	date = models.DateField(auto_now=False, auto_now_add=False)
	description = models.CharField(max_length=100)
	def __str__(self):  # Python 3: def __str__(self):
		return self.description

class Article(models.Model):
	pub_date = models.DateTimeField('Date Published')
	title = models.CharField(max_length=100)
	body = models.CharField(max_length=500)
	def __str__(self):  # Python 3: def __str__(self):
		return self.title

