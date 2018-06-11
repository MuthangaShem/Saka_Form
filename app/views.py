from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Profile,Event,Category
from django.contrib.auth.decorators import login_required

# Create your views here.
def event_dis(request):
    events = Event.objects.all()

    return render(request, 'event.html',{'events':events})
