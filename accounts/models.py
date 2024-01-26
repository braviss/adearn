from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notification(models.Model):

    STATUS_NOTIFICATION_CHOICES = [
        ("re", "Read"),
        ("un", "Unread"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS_NOTIFICATION_CHOICES, default='un')

    def __str__(self):
        return self.message