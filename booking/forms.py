from django import forms
from .models import BookATable

class BookATableForm(forms.ModelForm):
    class Meta:
        model = BookATable
        fields = ['firstname', 'lastname', 'email', 'date', 'time', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_date', 'class': 'form-control', 'placeholder': 'Select date'}),
            'time': forms.TimeInput(attrs={'id': 'id_time', 'class': 'form-control', 'placeholder': 'Select time', 'type': 'time'}),
        }        