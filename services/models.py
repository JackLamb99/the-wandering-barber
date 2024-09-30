from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()  # In minutes

    def __str__(self):
        return self.name
