from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),  # Welcome page at /bookings/
    path('list/', views.booking_list, name='booking_list'),  # Booking list at /bookings/list/
    path('new/', views.booking_create, name='booking_create'),
    path('success/', views.booking_success, name='booking_success'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
    path('<int:pk>/edit/', views.booking_update, name='booking_update'),
    path('<int:pk>/delete/', views.booking_delete, name='booking_delete'),
]