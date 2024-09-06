import logging
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import BookATable

logger = logging.getLogger(__name__)

@receiver(user_signed_up)
def handle_user_signed_up(sender, request, user, **kwargs):
    email = user.email
    logger.info(f"User signed up with email: {email}")

    # Hitta alla bokningar med samma e-post och där användarfältet är tomt
    bookings = BookATable.objects.filter(email=email, user__isnull=True)
    logger.info(f"Found {bookings.count()} bookings for this email")

    if bookings.exists():
        # Koppla dessa bokningar till den nyregistrerade användaren
        bookings.update(user=user)
        logger.info(f"Updated bookings for user: {user}")
    else:
        logger.info(f"No bookings found for email: {email}")