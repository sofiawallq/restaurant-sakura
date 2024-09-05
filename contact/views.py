from django.shortcuts import render
from django.contrib import messages
from .forms import ContactRestaurant


def contact_restaurant(request):
    """
    Handles the contact form for customers to send messages to the restaurant.
    Manages the display and submission of the contact form, allowing 
    customers to send inquiries. If the request method is POST and 
    form is valid, the message is saved to database and a success message 
    is displayed. Otherwise, the form is re-rendered.
    Returns either the contact form or a confirmation 
    if the form submission is successful.
    """
    contact_form = ContactRestaurant()

    if request.method == "POST":
        contact_form = ContactRestaurant(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS, "New message recieved.")
            return render(request, 'contact/contact_confirmation.html')

    return render(
        request,
        'contact/contact.html',
        {
            'contact_form': contact_form
        },
    )

