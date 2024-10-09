from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from services.models import Service
from .models import Appointment
from .forms import BookingForm


def booking(request):
    """ View to display the booking form and handle user input """

    # Handles AJAX request to get available time slots for a selected date
    if request.method == 'GET' and 'appointment_date' in request.GET:
        try:
            selected_date_str = request.GET['appointment_date']

            # Converts string date to datetime object
            selected_date = datetime.strptime(selected_date_str, '%d-%m-%Y').date()

            appointments_for_selected_date = Appointment.objects.filter(date=selected_date)

            # Booked time slots
            booked_time_slots = [appt.time.strftime('%H:%M') for appt in appointments_for_selected_date]
            available_time_slots = ['07:00', '10:00', '13:00']

            # Filters out booked time slots
            available_time_slots = [time for time in available_time_slots if time not in booked_time_slots]

            # Returns the available and booked time slots
            return JsonResponse({
                'available_time_slots': available_time_slots,
                'booked_time_slots': booked_time_slots
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Gets the selected date and time from the form
            selected_date = form.cleaned_data['appointment_date']
            selected_time = form.cleaned_data['selected_time']

            # Checks for existing appointment on the selected date and time
            existing_appointment = Appointment.objects.filter(date=selected_date, time=selected_time).exists()

            if existing_appointment:
                # Shows a message that the time is already booked
                messages.error(request, 'The selected time slot is already booked. Please choose another time.')
                return redirect('booking')

            # Proceeds with creating the appointment
            selected_services = form.cleaned_data['selected_services']
            address_1 = form.cleaned_data['address']
            address_2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            postcode = form.cleaned_data['postcode']
            total_price = form.cleaned_data['total_price']
            total_duration = form.cleaned_data['total_duration']

            # Manually adds Haircut service by default
            haircut_service = Service.objects.get(name="Haircut")
            selected_services.append(str(haircut_service.id))

            # Creates new appointment
            appointment = Appointment.objects.create(
                user=request.user,
                date=selected_date,
                time=selected_time,
                total_price=total_price,
                total_duration=total_duration,
                address_1=address_1,
                address_2=address_2,
                city=city,
                post_code=postcode,
                status='Booked'
            )

            # Adds services to appointment
            for service_id in selected_services:
                service = Service.objects.get(id=int(service_id))
                appointment.services.add(service)

            appointment.save()

            return redirect('confirm_booking', appointment_id=appointment.id)

    # Fallback: If no date selected, shows today's available time slots
    selected_date = timezone.now().date()
    appointments_today = Appointment.objects.filter(date=selected_date)
    booked_time_slots = [appt.time.strftime('%H:%M') for appt in appointments_today]

    # Available time slots for today
    available_time_slots = ['07:00', '10:00', '13:00']

    # Filters out already booked time slots
    available_time_slots = [
        time for time in available_time_slots if time not in booked_time_slots
    ]

    return render(request, 'appointments/booking.html', {
        'available_time_slots': available_time_slots,
        'booked_time_slots': booked_time_slots,
        'services': Service.objects.all(),
    })


@login_required
def confirm_booking(request, appointment_id):
    """ View to display the booking confirmation page """
    try:
        appointment = Appointment.objects.get(id=appointment_id, user=request.user)
    except Appointment.DoesNotExist:
        return redirect('booking')

    return render(request, 'appointments/confirmation.html', {
        'appointment': appointment,
    })
