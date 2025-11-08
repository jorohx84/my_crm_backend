from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    first_name = models.CharField(max_length=255, blank=True, default="")
    last_name = models.CharField(max_length=255, blank=True, default="")
    tel = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(max_length=50, blank=True, default="")
    last_logout = models.CharField(default='1900-01-01T00:00:00.000Z')
    last_inbox_check = models.CharField(default='1900-01-01T00:00:00.000Z')

