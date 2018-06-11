from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Profile,Event,Category,Location
from django.contrib.auth.decorators import login_required

# Create your views here.
def event_dis(request):
    event = Event.objects.all()

    return render(request, 'event.html')
