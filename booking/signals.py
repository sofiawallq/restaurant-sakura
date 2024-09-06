from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def handle_user_signed_up(sender, request, user, **kwargs):
    from .models import BookATable
    
    email = user.email
    bookings = BookATable.objects.filter(email=email, user__isnull=True)
    bookings.update(user=user)