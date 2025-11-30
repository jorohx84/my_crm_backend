from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver
from ..models import Task, Log
from message_app.models import Notification

@receiver(pre_save, sender=Task)
def stored_old_state(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        instance._old_state = old_instance.state


@receiver(post_save, sender=Task)

def create_notification_from_task(sender, instance, created, **kwargs):
    if created:
        notification = Notification.objects.create(
           
            text= "Neue Aufgabe wurde Ihrem Board hinzugefügt.",
            url=['main', 'singlecustomer', instance.customer.id, 'singletask', instance.id ],
           
        )
        notification.recipients.set(instance.members.all())



    else:
        old_type = getattr(instance, '_old_state', None)
        if old_type != 'released' and instance.state == 'released':
            notification = Notification.objects.create(
                
                text= "Aufgabe wurde freigegeben.",
                url=['main', 'singlecustomer', instance.customer.id, 'singletask', instance.id ],
        
            )
            notification.recipients.set(instance.members.all())  
      

# @receiver(m2m_changed, sender=Task.members.through)
# def notify_members_changed(sender, instance, action, pk_set, **kwargs):
#     if action in ['post_add', 'post_remove', 'post_clear']:
#         new_members = instance.members.all()
#         notification = Notification.objects.create(
#             text="Neue Aufgabe wurde Ihrem Board hinzugefügt.",
#             url=['main', 'singlecustomer', instance.customer.id, 'singletask', instance.id],
#         )
#         notification.recipients.set(new_members)

@receiver(m2m_changed, sender=Task.members.through)
def notify_members_changed(sender, instance, action, pk_set, **kwargs):
    # Nur auf Add-Aktionen reagieren
    if action == 'post_add' and pk_set:
        # Hole die User-Objekte für die neuen Mitglieder
        from django.contrib.auth import get_user_model
        User = get_user_model()
        new_members = User.objects.filter(pk__in=pk_set)

        notification = Notification.objects.create(
            text="Neue Aufgabe wurde Ihrem Board hinzugefügt.",
            url=['main', 'singlecustomer', instance.customer.id, 'singletask', instance.id],
        )
        notification.recipients.set(new_members)