from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Booking

# Create your views here.
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')  # redirect to success page
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'bookings/booking_success.html')


def booking_list(request):
    bookings = Booking.objects.all().order_by('-booking_date', '-booking_time')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_detail', pk=booking.pk)  # Redirect to detail page
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_form.html', {'form': form, 'update': True})