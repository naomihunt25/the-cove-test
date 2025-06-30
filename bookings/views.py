from django.shortcuts import render, redirect
from .forms import BookingForm

# Create your views here.
def booking_create_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')  # You can define this URL later
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})