from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import Event_Creation
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from .decorators import user_has_interests


@user_has_interests
def home(request):
    current_user = request.user
    if current_user.is_authenticated():
        user_interests = Profile.objects.get(profile_owner=current_user).profile_interest.all()
        events = Event.objects.filter(event_category__in=user_interests).all()
    events = Event.objects.all()
    categories = Category.objects.all()
    event_accordion = EventType.objects.all()

    return render(request, 'index.html', {'events': events, 'event_types': event_accordion, 'categories': categories})


def interests(request):

    interests = Category.objects.all()
    return render(request, 'interests.html', {'interests': interests})


@login_required
@user_has_interests
def create_event(request):

    current_user = request.user
    profile_instance = Profile.objects.get(profile_owner=current_user)

    if request.method == 'POST':
        form = Event_Creation(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.event_owner = profile_instance
            event.save()
            return redirect('home')
    else:
        form = Event_Creation()
    return render(request, 'create_event.html', {'form': form})


@login_required
@user_has_interests
def manage_event(request):

    current_user = request.user
    user_events = current_user.profile.event_set.all()

    form = Event_Creation()

    if request.method == "GET" and 'event_id' in request.GET and request.is_ajax():
        event_pk = request.GET.get('event_id')
        found_event = Event.objects.get(id=event_pk)

        update_form = Event_Creation(initial={'event_title': found_event.event_title, 'event_image': found_event.event_image,
                                              'event_location': found_event.event_location, 'event_category': found_event.event_category,
                                              'event_description': found_event.event_description, 'number_of_tickets': found_event.number_of_tickets, 'event_type': found_event.event_type, 'event_date': found_event.event_date})

        return render_to_response('ajax/update_modal.html', {'form': update_form})

    return render(request, 'manage_event.html', {'events': user_events})


@login_required
@user_has_interests
def update_event(request, event_id):

    if request.method == 'POST':
        instance = get_object_or_404(Event, id=event_id)
        form = Event_Creation(request.POST or None, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully')
    return redirect(reverse('event:manage_event'))


def ajax_search_event(request):

    if request.method == 'POST' and request.is_ajax():
        search_term = request.POST.get('search-term')
        results = Event.objects.filter(Q(event_title__icontains=search_term) | Q(
            event_location__icontains=search_term)).all()
    return render_to_response('ajax/searchresults.html', {"events": results})


@csrf_exempt
def ajax_accordion_redirect(request):

    if request.method == "POST" and 'event_pk' in request.POST and request.is_ajax():
        event_pk = request.POST['event_pk']
        found_event = EventType.objects.get(id=event_pk)
        results = found_event.event_set.all()
        return render_to_response('ajax/searchresults.html', {"events": results})

    if request.method == "POST" and 'category_pk' in request.POST and request.is_ajax():
        category_pk = request.POST['category_pk']
        found_category = Category.objects.get(id=category_pk)
        results = found_category.event_set.all()
        return render_to_response('ajax/searchresults.html', {"events": results})


@csrf_exempt
def ajax_handle_user_categories(request):

    current_user = request.user
    profile_instance = Profile.objects.get(id=request.user.id)
    if request.method == "POST" and 'category_arr' in request.POST and request.is_ajax():
        selected_list = json.loads(request.POST.get('category_arr'))
        profile_instance.profile_interest.set(selected_list)
        return redirect(reverse('home'))
        # return render_to_response('ajax/searchresults.html')


@login_required
@user_has_interests
def profile(request):

    current_user = request.user
    profile_details = User.objects.get(id=request.user.id)

    user = User.objects.get(id=current_user.id)

    update_form = ProfileUpdateForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(
        User, Profile, fields=('profile_interest', 'profile_location'))
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
                    return redirect(reverse('home'))

    return render(request, 'profile.html', {'profile_data': profile_details, "formset": formset, 'updated_user': update_form})
