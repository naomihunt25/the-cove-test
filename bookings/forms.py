from django import forms
from datetime import date, time
from .models import Booking

class BookingForm(forms.ModelForm):
    TIME_CHOICES = [
        # your valid booking times here
        (time(12, 0), '12:00 PM'),
        (time(12, 30), '12:30 PM'),
        # add more as needed...
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

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        today = date.today()
        if booking_date < today:
            raise forms.ValidationError("Booking date cannot be in the past.")
        return booking_date

    def clean_booking_time(self):
        booking_time = self.cleaned_data.get('booking_time')
        valid_times = [choice[0] for choice in self.TIME_CHOICES]
        if booking_time not in valid_times:
            raise forms.ValidationError("Please select a valid booking time.")
        return booking_time