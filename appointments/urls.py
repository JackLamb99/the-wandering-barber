from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.booking, name='booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel-booking/<int:appointment_id>/', views.cancel_booking, name='cancel_booking'),
    path('confirm/<int:appointment_id>/', views.confirm_booking, name='confirm_booking'),
]
