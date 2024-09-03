from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class BookingManager(models.Manager):
    def todays_bookings(self):
        return self.filter(date=timezone.now().date())

    def bookings_by_user(self, user):
        return self.filter(user=user)

    def bookings_for_time(self, date, time):
        return self.filter(date=date, time=time)


class BookATable(models.Model):
    """
    Stores a single booking made by site visitor.
    """
    TIMESLOT_CHOICES = [
        ("15:00", "3 PM"),
        ("16:00", "4 PM"),
        ("17:00", "5 PM"),
        ("18:00", "6 PM"),
        ("19:00", "7 PM"),
        ("20:00", "8 PM"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIMESLOT_CHOICES)
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)], default=1)
    message = models.TextField(blank=True, null=True)
    read = models.BooleanField(default=False)

    objects = BookingManager()

    def __str__(self):
        return f"Booking made by {self.lastname} on {self.date} at {self.time}"

    def clean(self):
        """
        Custom validation logic for the booking model.
        """
        # Get current date and time
        now = timezone.now()
        current_date = now.date()
        current_time = now.strftime("%H:%M")

        # Check if date or time is None
        if self.date is None or self.time is None:
            raise ValidationError("Correct date and time must be provided.")

        # Prevent booking in the past
        if self.date < current_date:
            raise ValidationError("You cannot book a table in the past.")
        elif self.date == current_date and self.time < current_time:
            raise ValidationError("You cannot book a table in the past.")

        # Verify that bookings are fetched correctly
        bookings_at_time = BookATable.objects.bookings_for_time(self.date, self.time)

        # Calculate total seats
        total_seats = sum(booking.guests for booking in bookings_at_time)

        if total_seats + self.guests > 100:
            raise ValidationError("No available tables for this time slot.")

    def save(self, *args, **kwargs):
        self.clean()  # Perform the validation check
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Table Booking"
        verbose_name_plural = "Table Bookings"
        ordering = ['-date', '-time']
        constraints = [
            models.UniqueConstraint(fields=['date', 'time', 'user'], name='unique_booking_per_user_per_time')
        ]