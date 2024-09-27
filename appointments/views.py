from django.shortcuts import render


# View for the booking page
def booking(request):
    return render(request, 'appointments/booking.html')  # Render booking.html


# View for the my_booking page
def my_booking(request):
    return render(request, 'appointments/my_booking.html')  # Render my_booking.html
