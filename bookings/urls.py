from django.urls import path
from . import views


urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('new/', views.booking_create, name='booking_create'),
    path('success/', views.booking_success, name='booking_success'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
    path('new/', views.booking_create, name='booking_create'),
    path('<int:pk>/edit/', views.booking_update, name='booking_update'),
]