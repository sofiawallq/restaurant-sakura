from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import BookATableForm
from .models import BookATable


def book_table(request):
    """
    Handles the creation of a new table booking.
    If the request method is POST it validates the form data, creates a new booking,
    associate it with the authenticated user if logged in. 
    Displays success or error messages accordingly.
    If the request method is GET, renders an empty booking form.
    Redirects to the booking confirmation page if form submission is successful.
    """
    if request.method == "POST":
        booking_form = BookATableForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            else:
                booking.user = None
            booking.save()

            return redirect('/booking/?success=true')
        else:
            messages.error(
                request, "There was an error with your reservation request." 
                "Please check the form and try again.")
    else:
        booking_form = BookATableForm()

    return render(
        request,
        'booking/booking.html',
        {'booking_form': booking_form}
    )


@login_required
def booking_list(request):
    """
    Displays a list of bookings made by the authenticated user.
    Requires user to be logged in. Fetches all bookings associated with user
    and displays them in a list format.
    """
    bookings = BookATable.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings': bookings})


@login_required
def booking_edit(request, booking_id):
    """
    Handles the editing of an existing booking.
    Requires user to be logged in. Fetches the booking by ID 
    and allows user to update it. If the request method is POST, 
    the form is validated, and if valid, the booking is updated.
    If GET, the form is pre-populated with the booking's current data.
    """
    booking = get_object_or_404(BookATable, id=booking_id, user=request.user)
    
    if request.method == "POST":
        form = BookATableForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
        else:
            message.error(
                request, "There was an error with updating your reservation")
    else:
        form = BookATableForm(instance=booking)

    return render(request, 'booking/booking_edit.html', {
            'form': form, 'booking': booking})


@login_required
def booking_delete(request, booking_id):
    """
    Handles the deletion of an existing booking.
    Fetches booking by ID and deletes it if the request method is POST.
    If successful, displays a success message and redirects to the booking list.
    """
    booking = get_object_or_404(BookATable, id=booking_id)
    if request.method == "POST":
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking/booking_delete.html', {'booking': booking})
