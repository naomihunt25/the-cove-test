from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.booking_date} at {self.booking_time}'