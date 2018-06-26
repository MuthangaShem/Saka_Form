from django.shortcuts import render, redirect, render_to_response, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from .decorators import user_has_interests
from django.utils.timezone import now
from django.conf import settings
from django.contrib import messages
import africastalking
import uuid
from .email import send_ticket_email, send_new_event_email


africas_key = settings.AFRICAS_KEY
africas_username = settings.AFRICAS_USERNAME
dt_now = str(now())


@user_has_interests
def home(request):

    current_user = request.user

    if current_user.is_authenticated():
        user_interests = Profile.objects.get(profile_owner=current_user).profile_interest.all()
        events = Event.objects.filter(event_category__in=user_interests,
                                      event_date__gt=dt_now).all()

    if current_user.is_anonymous():
        events = Event.objects.filter(event_date__gt=dt_now).all()
    categories = Category.objects.all()

    return render(request, 'index.html', {'events': events, 'categories': categories})


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

            tic_num = form.cleaned_data['number_of_tickets']

            existing_tickets = [num for sub in EventTicket.objects.values(
                'event_ticket_no') for num in sub]

            gen_tickets, start = [], 0

            while start < int(tic_num):
                random = uuid.uuid4().hex[:12].upper()

                if random not in existing_tickets:
                    gen_tickets.append(random)
                    start += 1
            g = gen_tickets

            for item in g:
                EventTicket.objects.bulk_create([EventTicket(event=event, event_ticket_no=item), ])

            # Email all subscribed user who are interested in that event category
            event_cat = [event.event_category]
            users = Profile.objects.filter(
                profile_interest__in=event_cat, profile_subscribed=True).all()

            subscribed_emails = [
                user.profile_owner.email for user in users if user.profile_owner.id is not current_user.id]

            for email in subscribed_emails:
                send_new_event_email(email, event)

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
                                              'event_description': found_event.event_description, 'number_of_tickets': found_event.number_of_tickets, 'event_date': found_event.event_date})

        return render(request, 'ajax/update_event.html', {'form': update_form, 'event_id': found_event.id})

    if request.method == "GET" and 'e_id' in request.GET and request.is_ajax():
        event_pk = request.GET.get('e_id')
        found_event = Event.objects.get(id=event_pk)

        form = PaymentGateway()
        return render(request, 'ajax/update_modal.html', {'form': form, 'event_name': found_event.event_title, 'event_id': found_event.id})

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


@login_required
@csrf_exempt
def register_event(request, event_id):

    current_user = request.user

    profile_instance = Profile.objects.get(profile_owner=current_user)

    this_event = Event.objects.get(id=event_id)

    form = PaymentGateway(request.POST or None, request.FILES)

    if form.is_valid():
        ticke = form.save(commit=False)
        ticke.profile = profile_instance
        ticke.event = this_event

        ticket_number = form.cleaned_data['number_of_tickets']

        if this_event.event_status == 'P':

            phone = '+254' + ''.join(list(form.cleaned_data['profile_phone'])[1:])

            ticket_charge = this_event.event_charges

            charges = int(ticket_charge) * int(ticket_number)

            africastalking.initialize(username=africas_username, api_key=africas_key)

            payment = africastalking.Payment

            ticke.save()

            payment.mobile_checkout(product_name='BusinessAcc',
                                    phone_number=phone, currency_code='KES', amount=charges, metadata={'event_booking_id': str(ticke.id), 'event_id': str(this_event.id), 'num_of_tck': str(ticket_number), 'profile_id': str(profile_instance.id)})

            messages.info(request, 'Please check your phone to confirm payment')

        if this_event.event_status == 'F':

            m = EventTicket.objects.filter(event=this_event, event_ticket_taken=False).values(
                'event_ticket_no')[:int(ticket_number)]

            taken_tck = [tck for kct in m for tck in kct.values()]

            ticke.ticket_confirmed = True
            ticke.save()

            EventTicket.objects.filter(event_ticket_no__in=taken_tck).update(
                event_ticket_taken=True, event_booking=ticke)

            data = TicketBooking.objects.filter(profile=profile_instance, event=this_event).all()
            send_ticket_email(profile_instance.profile_owner.email, data)
            messages.info(request, 'Check in your mail for Ticket(s)')

    return redirect('home')


@csrf_exempt
def africas_callback(request):

    callback = request.body

    callback_json = json.loads(callback)

    metadata = callback_json['requestMetadata']

    ticketbooking_id = metadata['event_booking_id']
    event_id = metadata['event_id']
    ticket_number = metadata['num_of_tck']
    profile_id = metadata['profile_id']

    profile_instance = Profile.objects.get(id=profile_id)
    this_event = Event.objects.get(id=event_id)
    ticke = TicketBooking.objects.get(id=ticketbooking_id)

    if callback_json['status'] == "Success":

        m = EventTicket.objects.filter(event=this_event, event_ticket_taken=False).values(
            'event_ticket_no')[:int(ticket_number)]

        taken_tck = [tck for kct in m for tck in kct.values()]

        ticke.ticket_confirmed = True
        ticke.save()

        EventTicket.objects.filter(event_ticket_no__in=taken_tck).update(
            event_ticket_taken=True, event_booking=ticke)

        data = TicketBooking.objects.filter(profile=profile_instance, event=this_event,
                                            ticket_confirmed=True).all()

        send_ticket_email(profile_instance.profile_owner.email, data)
        msg = "Ticket purchase successful. Check your email for tickets"

    if callback_json['status'] == "Failed":
        msg = "Ticket purchase unsuccessful!"

    messages.info(request, msg)

    return redirect(home)


def ajax_search_event(request):

    if request.method == 'POST' and request.is_ajax():
        search_term = request.POST.get('search-term')

        results = Event.objects.filter(Q(event_title__icontains=search_term, event_date__gt=dt_now) | Q(
            event_location__icontains=search_term, event_date__gt=dt_now)).all()

    return render(request, 'ajax/searchresults.html', {"events": results})


@csrf_exempt
def ajax_accordion_redirect(request):

    if request.method == "POST" and 'category_pk' in request.POST and request.is_ajax():

        category_pk = request.POST['category_pk']
        found_category = Category.objects.get(id=category_pk)
        results = found_category.event_set.filter(event_date__gt=dt_now).all()
        return render(request, 'ajax/searchresults.html', {"events": results})


@csrf_exempt
def ajax_handle_user_categories(request):

    current_user = request.user
    profile_instance = Profile.objects.get(id=request.user.id)
    if request.method == "POST" and 'category_arr' in request.POST and request.is_ajax():
        selected_list = json.loads(request.POST.get('category_arr'))
        profile_instance.profile_interest.set(selected_list)
        return redirect(reverse('home'))


@csrf_exempt
def ajax_calculate_ticket_cost(request):

    if request.method == "POST" and 'the_event' in request.POST and request.is_ajax():

        event_id = request.POST['the_event']
        ticket_number = request.POST['t_num']

        the_event = Event.objects.get(id=event_id)
        one_ticket = the_event.event_charges

        if the_event.event_status == 'P':
            charges = int(one_ticket) * int(ticket_number)

        if the_event.event_status == 'F':
            charges = 0

        return render(request, 'cost.html', {'total': charges})


@csrf_exempt
def ajax_subscribe_user(request):

    if request.method == "POST" and 'user_pk' in request.POST and request.is_ajax():

        user_id = request.POST['user_pk']

        profile = Profile.objects.get(id=user_id)

        if profile.profile_subscribed == True:

            Profile.objects.filter(id=user_id).update(profile_subscribed=False)

            status = "unsubscribed"

        if profile.profile_subscribed == False:

            Profile.objects.filter(id=user_id).update(profile_subscribed=True)

            status = "subscribed"

        status = json.dumps(status)

        return HttpResponse(status, content_type='application/json')


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
