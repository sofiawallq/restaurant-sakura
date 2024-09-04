from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import BookATable


class BookATableForm(forms.ModelForm):
    class Meta:
        model = BookATable
        fields = [
            'firstname', 'lastname', 'email', 'guests',
            'date', 'time', 'message']
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'date_picker', 'type': 'date'}),
            'time': forms.Select(choices=BookATable.TIMESLOT_CHOICES, attrs={
                'class': 'form-control', 'id': 'time_picker'}),
            'guests': forms.NumberInput(attrs={
                'class': 'form-control', 'min': '1', 'max': '8'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 4}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        today = timezone.now().date()
        if date < today:
            raise ValidationError("You cannot book a table in the past.")
        if date > today + timezone.timedelta(days=30):
            raise ValidationError(
                "You cannot book more than 30 days in advance.")
        return date

    def clean_time(self):
        date = self.cleaned_data.get('date')
        time = self.cleaned_data['time']
        now = timezone.now()
        current_time = now.strftime("%H:%M")

        if date == now.date() and time < current_time:
            raise ValidationError("You cannot book a table for a past time.")
        return time

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        guests = cleaned_data.get('guests')

        if date and time and guests:
            bookings_at_time = BookATable.objects.bookings_for_time(date, time)
            total_seats = sum(booking.guests for booking in bookings_at_time)
            if total_seats + guests > 100:
                raise ValidationError(
                    "No available tables for this time slot.")

        return cleaned_data
