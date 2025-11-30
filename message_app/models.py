from django.db import models
from django.conf import settings

class Notification(models.Model):
    recipients = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.JSONField(default=list)
    param = models.JSONField(default=dict)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"