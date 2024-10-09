from django.db import models
from django.contrib.auth.models import User
from services.models import Service


# Create your models here.
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Booked', 'Booked'),
        ('Canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    services = models.ManyToManyField(Service)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_duration = models.IntegerField()  # In minutes

    # Address fields
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='Booked')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment on {self.date} at {self.time} for {self.user}"
