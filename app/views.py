from django.shortcuts import render, redirect, render_to_response
from .models import *
from django.db.models import Q


# @login_required
def home(request):
    categories = Category.objects.all()
    events = Event.objects.all()

    return render(request, 'index.html', {'events': events, 'categories': categories, 'cat_list': cat_list})


def search_event(request):
    if request.method == 'POST' and request.is_ajax():
        search_term = request.POST.get('search-term')
        results = Event.objects.filter(Q(event_title__icontains=search_term) | Q(
            event_location__icontains=search_term)).all()
    return render_to_response('ajax/searchresults.html', {"results": results})
