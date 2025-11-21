import django_rq
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from profile_app.models import UserProfile
from .models import Account
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from rest_framework.authtoken.models import Token
from .utils import send_set_password_email

User = get_user_model()

@receiver(post_save, sender=Account)
def create_account_admin(sender, instance, created, **kwargs):
    if created:
        raw_password = get_random_string(12)

        email=instance.email
        user = User.objects.create(
            username = email,
            email=email,
            first_name='Accountadmin',
            last_name=instance.name,
            tenant=instance,
            is_staff=True,
            is_active=True,  
           
        )
        user.set_password(raw_password)
        user.save()


        UserProfile.objects.create(
            user=user,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            phone=instance.phone
        )
        token, created = Token.objects.get_or_create(user=user)
        print("Neuer Tenant-Admin:", email)
        print("Passwort:", raw_password)
        print("Token:", token.key)

        queue = django_rq.get_queue("default")
        queue.enqueue(send_set_password_email, user.pk)