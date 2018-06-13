
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import Event_Creation
from .models import *
from django.db.models import Q

# @login_required
def home(request):
	events = Event.objects.all()
	return render(request, 'index.html',{'events':events})



@login_required
def create_event(request):
	current_user = request.user
	if request.method == 'POST':
		form = Event_Creation(request.POST, request.FILES)
		if form.is_valid():
			event = form.save()
			event.User = current_user
			event.save()
			return redirect('home')
	else:
		form = Event_Creation()
	return render(request, 'create_event.html',{'form':form})

def search_event(request):
    if request.method == 'POST' and request.is_ajax():
        search_term = request.POST.get('search-term')
        results = Event.objects.filter(Q(event_title__icontains=search_term) | Q(
            event_location__icontains=search_term)).all()
    return render_to_response('ajax/searchresults.html', {"results": results})

