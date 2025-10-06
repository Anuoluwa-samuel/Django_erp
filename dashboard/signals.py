from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from notifications.signals import notify 

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()


User = get_user_model()

@receiver(post_save, sender=User)
def send_registration_notifications(sender, instance, created, **kwargs):
    if created:
        # --- Notify Admin ---
        subject_admin = "New User Registration Alert"
        message_admin = render_to_string("emails/admin_new_user.html", {
            "user": instance,
        })
        send_mail(
            subject_admin,
            strip_tags(message_admin),
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            html_message=message_admin,
        )

        # --- Notify User ---
        subject_user = "Account Created Successfully"
        message_user = render_to_string("emails/user_registration_success.html", {
            "user": instance,
        })
        send_mail(
            subject_user,
            strip_tags(message_user),
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            html_message=message_user,
        )

        # --- Optional Real-time Notification (django-notifications) ---
        # Notify Admin
        admin_user = User.objects.filter(is_superuser=True).first()
        if admin_user:
            notify.send(
                instance,
                recipient=admin_user,
                verb=f"New user '{instance.username}' just registered and awaits activation."
            )

        # Notify the User
        notify.send(
            admin_user,
            recipient=instance,
            verb="Your account has been created successfully. You will be notified once it is activated."
        )