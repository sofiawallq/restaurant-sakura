from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookATableForm
from .models import BookATable


def book_table(request):
    if request.method == "POST":
        booking_form = BookATableForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.add_message(request, messages.SUCCESS, "New guest reservation")
            return render(request, 'booking_confirmation.html', {'booking_form': booking_form})
    else:
        booking_form = BookATableForm()

    return render(
        request,
        'booking/booking.html',
        {
            'booking_form': booking_form
        }
    )

@login_required
def booking_list(request):
    bookings = BookATable.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings': bookings}) 


@login_required
def booking_edit(request, booking_id=None):
    if booking_id:
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    else:
        booking = None

    if request.method == "POST":
        form = BookATableForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  #Connect logged in user to reservation
            booking.save()
            messages.add_message(request, messages.SUCCESS, "Reservation updated successfully!")
            return redirect('booking_list')
    else:
        form = BookATableForm(instance=booking)

    return render(request, 'booking/booking_edit.html', {'form': form})  