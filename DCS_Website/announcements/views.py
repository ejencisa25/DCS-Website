from django.shortcuts import render
from announcements.models import Announcement

# Create your views here.
def announcement_details(request, pk):
	announcement = Announcement.objects.get(id=pk)
	context = {'announcement' : announcement}
	return render(request, 'announcements/announcements.html', context)