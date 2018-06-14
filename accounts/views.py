from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from social_django.models import UserSocialAuth
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from app.models import Profile
from .forms import *


class SignUp(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


@login_required
def settings(request):
    current_user = request.user
    profile_details = User.objects.get(id=request.user.id)

    user = User.objects.get(id=current_user.id)

    update_form = ProfileUpdateForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(
        User, Profile, fields=('profile_interest', 'profile_name',))
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


@login_required
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
