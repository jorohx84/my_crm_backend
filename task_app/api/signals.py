from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from ..models import Task
from message_app.models import Notification

@receiver(pre_save, sender=Task)
def stored_old_state(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        instance._old_state = old_instance.state


@receiver(post_save, sender=Task)

def create_notification_from_task(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.assignee,
            text= "Neue Aufgabe wurde Ihrem Board hinzugefügt.",
            url=['main', 'singlecustomer', instance.customer.id, 'task', instance.id ],
            param= {"type": instance.type}
        )

    if not created:
        old_type = getattr(instance, '_old_state', None)
        if old_type != 'released' and instance.state == 'released':
            Notification.objects.create(
                recipient=instance.assignee,
                text= "Aufgabe wurde freigegeben.",
                url=['main', 'singlecustomer', instance.customer.id, 'task', instance.id ],
                param= {"type": instance.type}
        )