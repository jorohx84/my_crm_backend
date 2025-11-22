from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255, blank=True, default="")
    last_name = models.CharField(max_length=255, blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, null=True, default="")
    email = models.EmailField(max_length=50, blank=True, default="")
    department = models.CharField(default="", null=True, blank=True)
    last_logout = models.CharField(default='1900-01-01T00:00:00.000Z')
    last_inbox_check = models.CharField(default='1900-01-01T00:00:00.000Z')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"