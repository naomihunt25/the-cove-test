from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Booking
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return render(request, 'bookings/home.html')

def about(request):
    return render(request, 'bookings/about.html')

def menu(request):
    return render(request, 'bookings/menu.html')

def contact(request):
    return render(request, 'bookings/contact.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'bookings/sign_up.html', {'form': form})

@login_required
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'bookings/booking_success.html')


def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

@login_required
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    # Permission check: only owner or staff can update
    if booking.user != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to edit this booking.")

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_form.html', {'form': form, 'update': True})

@login_required
@require_POST
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    # Permission check: only owner or staff can delete
    if booking.user != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to delete this booking.")

    booking.delete()
    return redirect('booking_list')

@login_required
def booking_list(request):
    if request.user.is_staff:
        bookings = Booking.objects.all().order_by('-booking_date', '-booking_time')
    else:
        bookings = Booking.objects.filter(user=request.user).order_by('-booking_date', '-booking_time')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')  # Redirect to homepage after logout
    return render(request, 'your_logout_template.html')  # Render the confirmation page for GET