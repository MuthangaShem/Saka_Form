from .models import Profile
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


def user_has_interests(function):
    def wrap(request, *args, **kwargs):
        current_user = request.user
        if current_user.is_authenticated():
            profile = Profile.objects.get(profile_owner=current_user)
            if not profile.profile_interest.all().count() >= 3:
                messages.info(request, 'Please select your interests to continue')
                return redirect(reverse('event:interests'))
            return function(request, *args, **kwargs)

        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
