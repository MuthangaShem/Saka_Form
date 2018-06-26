from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User


class UserSignUpForm(UserCreationForm):
    location = forms.CharField(max_length=254)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'location', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'E-mail Address'
        self.fields['location'].label = 'Your Location'
        self.fields['password1'].label = 'Account password'
        self.fields['password2'].label = 'Confirm account password'

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user._location = self.cleaned_data['location']
        if commit:
            user.save()

        return user


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email',)
