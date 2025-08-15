# core/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from inventory.models import Product
from purchases.models import PurchaseOrder

@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    """
    Automatically create default ERP groups and assign permissions after migrations.
    Runs only for relevant apps to avoid repeating unnecessarily.
    """
    # Only run for main/core app to avoid running multiple times
    if sender.name != 'erp_1_0':  
        return

    # Create main groups
    admin_group, _ = Group.objects.get_or_create(name='Admin')
    staff_group, _ = Group.objects.get_or_create(name='Staff')

    # Create module-specific groups
    inventory_manager_group, _ = Group.objects.get_or_create(name='Inventory Manager')
    purchase_officer_group, _ = Group.objects.get_or_create(name='Purchase Officer')

    # Give Inventory Manager permissions
    product_ct = ContentType.objects.get_for_model(Product)
    inventory_manager_group.permissions.add(
        Permission.objects.get_or_create(codename='view_product', name='Can view product', content_type=product_ct)[0],
        Permission.objects.get_or_create(codename='add_product', name='Can add product', content_type=product_ct)[0],
        Permission.objects.get_or_create(codename='change_product', name='Can change product', content_type=product_ct)[0],
    )

    # Give Purchase Officer permission
    purchase_ct = ContentType.objects.get_for_model(PurchaseOrder)
    approve_permission, _ = Permission.objects.get_or_create(
        codename='approve_purchaseorder',
        name='Can approve purchase order',
        content_type=purchase_ct
    )
    purchase_officer_group.permissions.add(approve_permission)

    print("✅ Default ERP roles and permissions have been created/updated.")
