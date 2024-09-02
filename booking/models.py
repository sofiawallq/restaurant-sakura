from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator

# Create your models here.
class BookATable(models.Model):
    """
    Stores a single booking made by site visitor.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking made by {self.lastname} on {self.date} at {self.time}"