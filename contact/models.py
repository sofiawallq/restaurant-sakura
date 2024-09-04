from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class ContactRestaurant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Question from {self.name}"
