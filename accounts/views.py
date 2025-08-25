from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Check functions
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_supervisor(user):
    return user.groups.filter(name='Supervisor').exists()

def is_staff(user):
    return user.groups.filter(name='Staff').exists()

def is_admin_or_supervisor(user):
    return user.is_superuser or user.groups.filter(name__in=["Admin", "Supervisor"]).exists()

def is_admin_or_supervisor(user):
    return user.is_superuser or user.groups.filter(name__in=["Admin", "Supervisor"]).exists()
