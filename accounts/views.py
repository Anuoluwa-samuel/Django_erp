from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render


# --- Check functions ---
def is_admin(user):
    return user.is_superuser or user.groups.filter(name="Admin").exists()

def is_inventory(user):
    return user.groups.filter(name__in=["Inventory Supervisor", "Inventory Staff"]).exists()

def is_purchases(user):
    return user.groups.filter(name__in=["Purchases Supervisor", "Purchases Staff"]).exists()


# --- Views ---
@login_required
@user_passes_test(is_inventory)
def inventory_dashboard(request):
    return render(request, "inventory/dashboard.html")

@login_required
@user_passes_test(is_purchases)
def purchases_dashboard(request):
    return render(request, "purchases/dashboard.html")

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "admin/dashboard.html")
