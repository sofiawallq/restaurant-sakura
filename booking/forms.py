from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import BookATable


class BookATableForm(forms.ModelForm):
    """
    Form for creating and validating table bookings.
    This form is based on the `BookATable` model and provides custom validation
    for the booking date, time, and availability of seats.
    Contains fields for:
        firstname (str) - first name of the person making the booking.
        lastname (str) - last name of the person making the booking.
        email (EmailField) - email address of the person making the booking.
        guests (int) - number of guests (between 1 and 8).
        date (DateField) - date of the booking.
        time (str) - time of the booking, chosen from predefined options.
        message (str) - optional message from the person making the booking.
    """
    policy_check = forms.BooleanField(
        required=True,
        label="I have read and agree to the Booking Policy",
        error_messages={'required': 'You must agree to the booking policy to proceed.'}
    )

    class Meta:
        model = BookATable
        fields = [
            'firstname', 'lastname', 'email', 'guests',
            'date', 'time', 'message'
        ]
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
        """
        Validates the booking date.
        Ensures that the booking date is not in the past and not more than
        30 days in the future.
        Raises ValidationError if the date is in the past or more 
        than 30 days ahead.
        """
        date = self.cleaned_data['date']
        today = timezone.now().date()
        if date < today:
            raise ValidationError("You cannot book a table in the past.")
        if date > today + timezone.timedelta(days=30):
            raise ValidationError(
                "You cannot book more than 30 days in advance.")
        return date

    def clean_time(self):
        """
        Validate the booking time.
        Ensures that the time selected is not in the past if the booking
        is for the current day.
        Raises ValidationError if the time is earlier 
        than current time for todays bookings.
        """
        date = self.cleaned_data.get('date')
        time = self.cleaned_data['time']
        now = timezone.now()
        current_time = now.strftime("%H:%M")

        if date == now.date() and time < current_time:
            raise ValidationError("You cannot book a table for a past time.")
        return time

    def clean(self):
        """
        Performs full form validation, including checking seat availability.
        Combines the date, time, and number of guests to check if there are available
        seats for chosen time slot.
        Raises ValidationError if there are no available seats.
        """
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
