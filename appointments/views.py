from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from services.models import Service
from .models import Appointment
from .forms import BookingForm


def booking(request):
    """ View to display the booking form and handle user input """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Gets cleaned data from the form
            selected_date = form.cleaned_data['appointment_date']
            selected_time = form.cleaned_data['selected_time']
            selected_services = form.cleaned_data['selected_services']
            address_1 = form.cleaned_data['address']
            address_2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            postcode = form.cleaned_data['postcode']
            total_price = form.cleaned_data['total_price']
            total_duration = form.cleaned_data['total_duration']

            # Manually adds Haircut service to the selected_services list
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
            # for service_id in selected_services:
            #     try:
            #         service = Service.objects.get(id=int(service_id))
            #         appointment.services.add(service)
            #     except Service.DoesNotExist:
            #         print(f"Service with id {service_id} does not exist.")
            # appointment.save()

            # Redirects to confirmation page
            return redirect('confirm_booking', appointment_id=appointment.id)
        else:
            print(form.errors)
    else:
        form = BookingForm()  # Shows empty form for GET requests

    # Gets available time slots
    available_time_slots = ['07:00', '10:00', '13:00']
    appointments_today = Appointment.objects.filter(date=timezone.now().date())

    # Determines which time slots are already booked
    booked_time_slots = [appt.time.strftime('%H:%M') for appt in appointments_today]

    # Filters available slots
    available_time_slots = [
        time for time in available_time_slots if time not in booked_time_slots
    ]

    return render(request, 'appointments/booking.html', {
        'form': form,
        'available_time_slots': available_time_slots,
        'services': Service.objects.all()
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
