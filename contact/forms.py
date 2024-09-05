from django import forms
from .models import ContactRestaurant


class ContactRestaurant(forms.ModelForm):
    class Meta:
        model = ContactRestaurant
        fields = ('subject', 'name', 'email', 'message')
