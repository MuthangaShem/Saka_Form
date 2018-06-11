from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import Event_Creation



# @login_required
def home(request):
    return render(request, 'index.html')


@login_required
def create_event(request):
	current_user = request.user
	if request.method == 'POST':
		form = Event_Creation(request.POST, request.FILES)
		if form.is_valid():
			event = form.save(commit=False)
			event.user = current_user
			event.save()
			return redirect('home')
	else:
		form = Event_Creation()
	return render(request, 'create_event.html',{'form':form})
