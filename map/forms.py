from django import forms
from django.forms import ModelForm
from .models import Schedule

# Create the form class.

class DateTimeInput (forms.DateTimeInput):
    input_type='datetime-local'

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['checkin_datetime', 'checkout_datetime', 'phone_number']
        widgets = {
            # 'checkin_datetime' : DateTimeInput(),
            # 'checkout_datetime' : DateTimeInput(),
        }
        labels = {
            'checkin_datetime' : "Entrada",
            'checkout_datetime' : "Salida",
            'phone_number' : "Nro. de teléfono (*)"
        }