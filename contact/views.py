from django.shortcuts import render
from django.contrib import messages
from .forms import ContactRestaurant

# Create your views here.
def contact_restaurant(request):
    contact_form = ContactRestaurant()

    if request.method == "POST":
        contact_form = ContactRestaurant(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "New message recieved.")
            return HttpResponse("Message received! We will get back to you as soon as possible!")

    return render(
        request, 
        'contact/contact.html',
        {
            'contact_form': contact_form
        },
    )


    