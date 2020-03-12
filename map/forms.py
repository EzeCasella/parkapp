from django import forms
from django.forms import ModelForm
from .models import Schedule

# Create the form class.

class DateInput (forms.DateInput):
    input_type='date'

class TimeInput (forms.TimeInput):
    input_type='time'

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['checkin_date', 'checkin_time', 'checkout_date', 'checkout_time', 'phone_number']
        widgets = {
            'checkin_date' : DateInput(),
            'checkin_time' : TimeInput(),
            'checkout_date' : DateInput(),
            'checkout_time' : TimeInput(),

        }
        labels = {
            'phone_number' : "Nro. de teléfono (*)"
        }