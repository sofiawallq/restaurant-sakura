from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from .models import BookATable

class BookATableForm(forms.ModelForm):
    class Meta:
        model = BookATable
        fields = ['firstname', 'lastname', 'email', 'date', 'time', 'message']
        widgets = {
            'date': DatePickerInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'placeholder': 'Select date'}
            ),
            'time': TimePickerInput(
                format='%H:%M',
                attrs={'class': 'form-control', 'placeholder': 'Select time'}
            ),
        }          

             