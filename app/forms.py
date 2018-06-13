from django import forms
from .models import Event


class Event_Creation(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_title',
                  # 'event_description',
                  'event_category',
                  'event_location',
                  'number_of_tickets',
                  'event_type',
                  )
