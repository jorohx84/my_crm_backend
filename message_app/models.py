from django.db import models
from django.conf import settings

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="system_messages")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.JSONField(default=list)
    param = models.JSONField(default=dict)
    is_read = models.BooleanField(default=False)
