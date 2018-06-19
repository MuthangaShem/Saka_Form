from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from .models import Event
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class Event_Creation(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_title', 'event_image', 'event_location', 'event_category', 'event_status',
                  'event_charges', 'event_description', 'number_of_tickets', 'event_type', 'event_date',)
        widgets = {
                  'event_date': DateInput()
                  }


        def __init__(self, data=None, *args, **kwargs):
          super().__init__(data, *args, **kwargs)
          self.fields['event_charges'].required = False
          if data and data.get('event_status', None) == 'P':
            self.fields['event_charges'].required = True
