from django.db import models
from contact_app.models import Contact
from customer_app.models import Customer
from profile_app.models import UserProfile
from django.conf import settings
class Activity(models.Model):
    TYPE_CHOICES = (
        ('call', 'Call'),
        ('invite', 'Invite'),
        ('video', 'Video'),
        ('email', 'Email'),
    )
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="contact_activities")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_activities")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_activities")
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=45, default='ActivityTitle')
    description = models.TextField()
    type = models.CharField(choices=TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=False, auto_now=False)