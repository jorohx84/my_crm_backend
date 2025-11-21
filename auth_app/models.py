from django.contrib.auth.models import AbstractUser
from django.db import models
from account_app.models import Account

class User(AbstractUser):
    tenant = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="users", null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True) 

