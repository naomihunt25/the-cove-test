from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.booking_create_view, name='booking_create'),
    path('success/', views.booking_success_view, name='booking_success'),
]