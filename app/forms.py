from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from .models import Event


class Event_Creation(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_title',
                  # 'event_description',
                  # 'event_category',
                  'event_location',
                  'number_of_tickets',
                  'event_type',
                  )
        exclude = ('event_owner',
                   'event_created_on',
                   'event_image')
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
