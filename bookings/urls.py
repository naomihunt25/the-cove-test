from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.booking_create, name='booking_create_view'),
    path('success/', views.booking_success, name='booking_success'),  
]