from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    areacode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
