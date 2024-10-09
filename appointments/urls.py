from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.booking, name='booking'),  # Booking page
    path('confirm/<int:appointment_id>/', views.confirm_booking, name='confirm_booking'),  # Booking Confirmation page
]
