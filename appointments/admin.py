from django.contrib import admin
from .models import Appointment
from .models import AppointmentService


# Register your models here.
admin.site.register(Appointment)
admin.site.register(AppointmentService)
