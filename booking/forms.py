from django import forms
from .models import BookATable

class BookATableForm(forms.ModelForm):
    class Meta:
        model = BookATable
        fields = ['firstname', 'lastname', 'email', 'guests', 'date', 'time', 'message']         
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'date_picker'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'id': 'time_picker'}),
        }

             