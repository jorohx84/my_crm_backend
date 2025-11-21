from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

def send_set_password_email(user_pk):
    try:
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        return

    # Token + UID
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_url = f"{settings.FRONTEND_URL}/set-password/{uidb64}/{token}/"

    subject = "Dein Zugang - Setze dein Passwort"

    # Plain-Text
    text_content = f"""
            Hallo {user.first_name or user.username},

            Ein Zugang für dich wurde erstellt. Bitte setze dein Passwort über folgenden Link:

            {reset_url}

            Der Link ist einmalig gültig und läuft nach kurzer Zeit ab.
            Falls du diese Mail nicht angefordert hast, ignoriere sie bitte.
            """

                # HTML-Mail direkt in Python
    html_content = f"""
            <html>
            <body style="font-family: sans-serif; line-height:1.5;">
            <h2>Hallo {user.first_name or user.username},</h2>
            <p>Ein Zugang für dich wurde erstellt. Bitte setze dein Passwort über den folgenden Link:</p>
            <p>
                <a href="{reset_url}" style="display:inline-block; padding:10px 15px; background-color:#1a73e8; color:white; text-decoration:none; border-radius:4px;">Passwort setzen</a>
            </p>
            <p>Der Link ist einmalig gültig und läuft nach kurzer Zeit ab.<br>
            Falls du diese Mail nicht angefordert hast, ignoriere sie bitte.</p>
            </body>
            </html>
            """

    # E-Mail senden
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)



def send_manual_reset_password_email(user_pk):
    """
    E-Mail für manuelles Passwort-Reset (Admin-Initiated)
    """
    try:
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        return

    # Token + UID
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_url = f"{settings.FRONTEND_URL}/set-password/{uidb64}/{token}/"

    subject = "Passwort zurücksetzen angefordert"
    
    # Plain-Text
    text_content = f"""
            Hallo {user.first_name or user.username},

            Ein Administrator hat ein Zurücksetzen Ihres Passworts angefordert. 
            Bitte setzen Sie Ihr Passwort über folgenden Link:

            {reset_url}

            Der Link ist einmalig gültig und läuft nach kurzer Zeit ab.
            Falls Sie diese Aktion nicht angefordert haben, wenden Sie sich bitte an Ihren Administrator.
                """

                # HTML-Mail
    html_content = f"""
            <html>
            <body style="font-family: sans-serif; line-height:1.5;">
            <h2>Hallo {user.first_name or user.username},</h2>
            <p>Ein Administrator hat ein Zurücksetzen Ihres Passworts angefordert.</p>
            <p>
                <a href="{reset_url}" style="display:inline-block; padding:10px 15px; background-color:#d93025; color:white; text-decoration:none; border-radius:4px;">Passwort zurücksetzen</a>
            </p>
            <p>Der Link ist einmalig gültig und läuft nach kurzer Zeit ab.<br>
            Falls Sie diese Aktion nicht angefordert haben, wenden Sie sich bitte an Ihren Administrator.</p>
            </body>
            </html>
            """

    # E-Mail versenden
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)
