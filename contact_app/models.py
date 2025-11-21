from django.db import models
from customer_app.models import Customer
from profile_app.models import UserProfile
from django.conf import settings
class Contact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_contact")
    name = models.CharField(max_length=255) 
    position = models.CharField(max_length=255) 
    function = models.CharField(max_length=255) 
    department = models.CharField(max_length=255) 
    phone = models.CharField(max_length=255) 
    email = models.EmailField()
    notes = models.TextField(default='', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contact_created_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contact_updated_by", blank=True, null=True)
    last_contact = models.DateTimeField(blank=True, null=True)
    last_contact_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contact_last_contact_by", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    newsletter_opt_in = models.BooleanField(default=True)