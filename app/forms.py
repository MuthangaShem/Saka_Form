from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from .models import Event
from django.contrib.auth.models import User


class Event_Creation(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_title',
                  # 'event_description',
                  # 'event_category',
                  'event_image',
                  'event_location',
                  'number_of_tickets',
                  'event_type',
                  'event_date',
                  )
        widgets = {
            'event_date': DateTimePickerInput(
                options={
                    "format": "MM/DD/YYYY",  # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
            ),
        }
