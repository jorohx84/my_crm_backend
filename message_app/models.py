from django.db import models
from profile_app.models import UserProfile

class Notification(models.Model):
    recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="system_messages")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.JSONField(default=list)
    param = models.JSONField(default=dict)
    is_read = models.BooleanField(default=False)
