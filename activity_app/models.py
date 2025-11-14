from django.db import models
from contact_app.models import Contact
from customer_app.models import Customer
from profile_app.models import UserProfile

class Activity(models.Model):
    TYPE_CHOICES = (
        ('call', 'Call'),
        ('invite', 'Invite'),
        ('video', 'Video'),
        ('email', 'Email'),
    )
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="contact_activities")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_activities")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user_activities")
    description = models.TextField()
    type = models.CharField(choices=TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=False, auto_now=False)