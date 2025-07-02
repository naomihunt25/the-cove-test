from django import forms
from datetime import date, time
from .models import Booking

class BookingForm(forms.ModelForm):
    TIME_CHOICES = [
        # your valid booking times here
        (time(12, 0), '12:00 PM'),
        (time(12, 30), '12:30 PM'),
        (time(13, 0), '1:00 PM'),
        (time(13, 30), '1:30 PM'),
        (time(14, 0), '2:00 PM'),
        (time(14, 30), '2:30 PM'),
        (time(15, 0), '3:00 PM'),
        (time(15, 30), '3:30 PM'),
        (time(16, 0), '4:00 PM'),
        (time(16, 30), '4:30 PM'),
        (time(17, 0), '5:00 PM'),
        (time(17, 30), '5:30 PM'),
        (time(18, 0), '6:00 PM'),
        (time(18, 30), '6:30 PM'),
        (time(19, 0), '7:00 PM'),
        (time(19, 30), '7:30 PM'),
        (time(20, 0), '8:00 PM'),
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
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': date.today().isoformat()}),
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
        if isinstance(booking_time, str):
            booking_time = datetime.strptime(booking_time, "%H:%M").time()  # convert string to time object
        valid_times = [choice[0] for choice in self.TIME_CHOICES]
        if booking_time not in valid_times:
            raise forms.ValidationError("Please select a valid booking time.")
        return booking_time