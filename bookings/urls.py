from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Static pages
    path('', views.home, name='home'),               # /
    path('about/', views.about, name='about'),       # /about/
    path('menu/', views.menu, name='menu'),          # /menu/
    path('contact/', views.contact, name='contact'), # /contact/

    # Booking-related URLs
    path('bookings/new/', views.booking_form, name='booking_form'),
    path('bookings/success/', views.booking_success, name='booking_success'), # /bookings/success/
    path('bookings/<int:pk>/', views.booking_detail, name='booking_detail'),  # /bookings/1/
    path('bookings/<int:pk>/edit/', views.booking_update, name='booking_update'),  # /bookings/1/edit/
    path('bookings/<int:pk>/delete/', views.booking_delete, name='booking_delete'),  # /bookings/1/delete/
    path('bookings/', views.booking_list, name='booking_list'),  # /bookings/

    # Auth URLs - login/logout/sign_up all here
    path('accounts/login/', auth_views.LoginView.as_view(template_name='bookings/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/sign_up/', views.sign_up, name='sign_up'),
]