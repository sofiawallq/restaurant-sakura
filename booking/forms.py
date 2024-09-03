from django import forms
from .models import BookATable
import datetime

class BookATableForm(forms.ModelForm):
    class Meta:
        model = BookATable
        fields = ['firstname', 'lastname', 'email', 'guests', 'date', 'time', 'message']         
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'date_picker'}),
            # 'time': forms.TimeInput(attrs={'class': 'form-control', 'id': 'time_picker'}),
        }


    time_choices = [(datetime.time(hour, minute), f'{hour:02d}:{minute:02d}')
                    for hour in range(15, 23)
                    for minute in (0, 30)]

    time = forms.ChoiceField(choices=time_choices, widget=forms.Select(attrs={'class': 'form-control', 'id': 'time_picker'}))        

             