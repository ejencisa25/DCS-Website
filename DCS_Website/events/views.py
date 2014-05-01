from django.shortcuts import render
from events.models import Event

# Create your views here.
def event_details(request, pk):
	event = Event.objects.get(id=pk)
	context = {'event' : event}
	return render(request, 'events/events.html', context)