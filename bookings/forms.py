from django import forms
from datetime import time
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
    'first_name': forms.TextInput(attrs={'class': 'form-control'}),
    'last_name': forms.TextInput(attrs={'class': 'form-control'}),
    'email': forms.EmailInput(attrs={'class': 'form-control'}),
    'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
    'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
}
        

    def clean_booking_time(self):
        booking_time = self.cleaned_data['booking_time']

        if not (time(12, 0) <= booking_time <= time(20, 0)):
            raise forms.ValidationError("Time must be between 12:00 and 20:00.")

        if booking_time.minute % 15 != 0 or booking_time.second != 0:
            raise forms.ValidationError(
                "Please choose a time in 15-minute intervals, e.g., 12:00, 12:15, 12:30."
            )

        return booking_time