from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from .models import Event
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class Event_Creation(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_title',
                  'event_image',
                  'event_location',
                  'event_category',
                  'event_description',
                  'number_of_tickets',
                  'event_type',
                  'event_date',]

        widgets = {
                  'event_date': DateInput(),
        }

