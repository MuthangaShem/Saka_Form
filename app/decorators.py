from .models import Profile
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


def user_has_interests(function):
    def wrap(request, *args, **kwargs):
        current_user = request.user
        profile = Profile.objects.get(profile_owner=current_user)
        if current_user.is_authenticated():
            if not profile.profile_interest.all():
                messages.info(request, 'Please select your interests to continue')
                return redirect(reverse('event:interests'))
        else:
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
