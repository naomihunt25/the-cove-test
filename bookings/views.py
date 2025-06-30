from django.shortcuts import render, redirect
from .forms import BookingForm

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
