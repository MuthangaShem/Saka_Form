from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import Event_Creation
from .models import *
from django.db.models import Q


# @login_required
def home(request):
    categories = Category.objects.all()
    events = Event.objects.all()

    return render(request, 'index.html', {'events': events, 'categories': categories})


@login_required
def create_event(request):
    current_user = request.user
    profile_instance = Profile.objects.get(profile_owner=current_user)
    if request.method == 'POST':
        form = Event_Creation(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            # event.user = current_user
            event_owner = profile_instance
            event.save()
            return redirect('home')
    else:
        form = Event_Creation()
    return render(request, 'create_event.html', {'form': form})


def search_event(request):
    if request.method == 'POST' and request.is_ajax():
        search_term = request.POST.get('search-term')
        results = Event.objects.filter(Q(event_title__icontains=search_term) | Q(
            event_location__icontains=search_term)).all()
    return render_to_response('ajax/searchresults.html', {"results": results})


@login_required
def profile(request):
    current_user = request.user
    profile_details = User.objects.get(id=request.user.id)

    user = User.objects.get(id=current_user.id)

    update_form = ProfileUpdateForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(
        User, Profile, fields=('profile_photo', 'profile_id',))
    formset = ProfileInlineFormset(instance=user)

    if current_user.is_authenticated() and current_user.id == user.id:
        if request.method == "POST":
            update_form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if update_form.is_valid():
                updated_user = update_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=current_user)

                if formset.is_valid():
                    updated_user.save()
                    formset.save()
                    return redirect(index)

    return render(request, 'profile.html', {'profile_data': profile_details, "formset": formset, 'updated_user': update_form})
