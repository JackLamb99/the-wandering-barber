from django.db import models
from users.models import User


# Create your models here.
class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key relationship
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user}: {self.rating}/5"
