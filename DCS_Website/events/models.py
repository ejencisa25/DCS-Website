from django.db import models

# Create your models here.
class Event(models.Model):
	date = models.DateField(auto_now=False, auto_now_add=False)
	description = models.CharField(max_length=100)
	def __str__(self):  # Python 3: def __str__(self):
		return self.description