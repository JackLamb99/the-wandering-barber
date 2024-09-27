from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),  # Booking page
    path('my_booking/', views.my_booking, name='my_booking'),  # My Booking page
]
