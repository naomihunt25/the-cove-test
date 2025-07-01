from django.urls import path
from . import views

app_name = 'bookings'  # for namespacing URLs

urlpatterns = [
    path('new/', views.booking_create, name='booking_create'),  # booking form at /bookings/new/
    path('success/', views.booking_success, name='booking_success'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
    path('<int:pk>/edit/', views.booking_update, name='booking_update'),
    path('<int:pk>/delete/', views.booking_delete, name='booking_delete'),
    path('', views.booking_list, name='booking_list'),
]