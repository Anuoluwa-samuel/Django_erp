from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group
from django.dispatch import receiver

@receiver(post_migrate)
def create_roles(sender, **kwargs):
    if sender.name == "accounts":  # only run when this app migrates
        roles = ["Admin", "Supervisor", "Staff"]
        for role in roles:
            Group.objects.get_or_create(name=role)
