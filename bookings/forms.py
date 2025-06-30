from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'phone_number', 
            'booking_date', 
            'booking_time', 
            'message',
        ]
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }