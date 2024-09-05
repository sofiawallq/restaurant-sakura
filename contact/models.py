from django.db import models
from cloudinary.models import CloudinaryField


class ContactRestaurant(models.Model):
    """
    Model to store customer inquiries/messages sent to the restaurant.
    Holds details such as subject, sender's name, email, and message content. 
    It also includes a 'read' field to track whether the message 
    has been marked as read by the site admin in the admin panel.
    Contains fields for:
        subject (str) - subject of the inquiry.
        name (str) - name of the person sending the message.
        email (EmailField) - email address of the sender.
        message (TextField) - body of the message or inquiry.
        read (bool) - Indicates if the message has been marked as read.
    """
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Question from {self.name}"
