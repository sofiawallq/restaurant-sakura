from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class BookATable(models.Model):
    """
    Stores a single booking made by site visitor.
    """
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking made by {self.name} on {self.date} at {self.time}"
