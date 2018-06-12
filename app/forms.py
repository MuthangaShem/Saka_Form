from django import forms
from .models import Event



class Event_Creation(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('event_owner',
        			'event_created_on',
        			'event_image')