from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from notifications.signals import notify
from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Automatically create or update a user profile whenever a User is saved."""
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


@receiver(post_save, sender=User)
def send_registration_notifications(sender, instance, created, **kwargs):
    """Send email + real-time notifications upon user registration."""
    if not created:
        return  # Only send for newly created users

    try:
        # --- 1️⃣ Notify Admin ---
        subject_admin = "New User Registration Alert"
        message_admin = render_to_string("admin_new_user.html", {
            "user": instance,
        })
        send_mail(
            subject_admin,
            strip_tags(message_admin),
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            html_message=message_admin,
            fail_silently=True,  # Prevents crashing if email fails
        )

        # --- 2️⃣ Notify User ---
        subject_user = "Account Created Successfully"
        message_user = render_to_string("user_registration_success.html", {
            "user": instance,
        })
        if instance.email:  
            send_mail(
                subject_user,
                strip_tags(message_user),
                settings.DEFAULT_FROM_EMAIL,
                [instance.email],
                html_message=message_user,
                fail_silently=True,
            )

        # --- 3️⃣ Real-time Notifications (django-notifications-hq) ---
        admin_user = User.objects.filter(is_superuser=True).first()
        if admin_user:
            # Notify Admin
            notify.send(
                instance,
                recipient=admin_user,
                verb=f"New user '{instance.username}' just registered and awaits activation."
            )

            # Notify User
            notify.send(
                admin_user,
                recipient=instance,
                verb="Your account has been created successfully. You will be notified once it is activated."
            )

    except BadHeaderError:
        print("⚠️ Invalid header found while sending email.")
    except Exception as e:
        # Always print error in dev so you know what happened
        import traceback
        print("⚠️ Error in send_registration_notifications:", traceback.format_exc())
