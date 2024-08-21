from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from .models import BookATable

class BookATableForm(forms.ModelForm):
    class Meta:
        model = BookATable
        fields = ['firstname', 'lastname', 'email', 'date', 'time', 'message']         
        widgets = {
            'date': DatePickerInput(options={"format": "YYYY-MM-DD", "placeholder": "Select date"}),
            'time': TimePickerInput(options={"format": "HH:mm", "placeholder": "Select time"}),
        }

             