# core/signals.py
from django.db.models.signals import post_migrate, post_save
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver

from inventory.models import Product, Order
from purchases.models import PurchaseRequest

@receiver(post_migrate)
def create_general_user_group(sender, **kwargs):
    general_group, _ = Group.objects.get_or_create(name='General User')

    # Assign only basic permissions
    allowed_models = [Product, Order, PurchaseRequest]

    for model in allowed_models:
        content_type = ContentType.objects.get_for_model(model)
        perms = Permission.objects.filter(content_type=content_type).exclude(codename__startswith='delete_')
        general_group.permissions.add(*perms)

    print("✅ General User group created with limited permissions")

@receiver(post_save, sender=User)
def assign_general_user_group(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        general_group = Group.objects.get(name='General User')
        instance.groups.add(general_group)
