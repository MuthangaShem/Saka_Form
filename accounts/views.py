from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
# <<<<<<< HEAD

# from . import forms

# # Create your views here.
# =======
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from social_django.models import UserSocialAuth

from . import forms
# >>>>>>> 5621387e0888a58f5dc24579ce31704187eb6729


class SignUp(CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
# <<<<<<< HEAD
# =======

# @login_required


def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    try:
        google_login = user.social_auth.get(provider='google')
    except UserSocialAuth.DoesNotExist:
        google_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'accounts/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'google_login': google_login,
        'can_disconnect': can_disconnect
    })


# @login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'accounts/password.html', {'form': form})
# >>>>>>> 5621387e0888a58f5dc24579ce31704187eb6729
