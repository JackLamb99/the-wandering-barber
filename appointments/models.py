from django.db import models
from django.contrib.auth.models import User
from services.models import Service


# Create your models here.
class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20)  # Booked or Canceled
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_duration = models.IntegerField()  # In minutes
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key relationship
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment on {self.date} at {self.time} for {self.user}"


class AppointmentService(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('appointment', 'service'),)  # Prevent duplicates

    def __str__(self):
        return f"{self.service} for {self.appointment}"
