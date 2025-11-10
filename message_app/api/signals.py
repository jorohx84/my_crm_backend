from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync

from ..models import Notification
from channels.layers import get_channel_layer
channel_layer = get_channel_layer()


@receiver(post_save, sender=Notification)
def notify_via_websocket(sender, instance, created, **kwargs):
       
        print(f"Signal ausgelöst: id={instance.id}, created={created}, is_read={instance.is_read}")
        group_name = f'notifications_{instance.recipient.id}'
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "send_notification",
                "message": {
                    "id": instance.id,
                    "text": instance.text,
                    "url": instance.url,
                    "param": instance.param,
                    "is_read": instance.is_read,
                    "created_at": str(instance.created_at)
                }
            }
        )