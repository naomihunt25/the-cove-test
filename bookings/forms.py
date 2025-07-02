from django import forms
from datetime import time
from .models import Booking

class BookingForm(forms.ModelForm):
    TIME_CHOICES = [
        # define your allowed booking times here if needed
        # example:
        (time(12, 0), '12:00 PM'),
        (time(12, 30), '12:30 PM'),
        # add other times as needed...
    ]

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
            'booking_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }

    def clean_booking_time(self):
        booking_time = self.cleaned_data.get('booking_time')
        valid_times = [choice[0] for choice in self.TIME_CHOICES]
        if booking_time not in valid_times:
            raise forms.ValidationError("Please select a valid booking time.")
        return booking_time