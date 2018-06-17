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
<<<<<<< HEAD
                  ]
        widgets = {
                  'event_date': DateInput(),
        }

        # widgets = {'event_date': DateTimePickerInput(attrs={'class': 'datepicker'})}
        # widgets = {
        #     'event_date': DateTimePickerInput(
        #         options={
        #             "format": "MM/DD/YYYY",  # moment date-time format
        #             "showClose": True,
        #             "showClear": True,
        #             "showTodayButton": True,
        #         }
        #     ),
        # }
=======
                  'event_date',
                  )
>>>>>>> ba299aa0c502e58a7c53e3bf18136cf3ad2ccf23
