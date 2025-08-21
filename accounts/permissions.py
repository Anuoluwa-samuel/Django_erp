from django.http import HttpResponseForbidden
from rest_framework import permissions

def group_required(allowed_groups=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            # 1. Must be logged in
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Login required")

            # 2. Must be in one of the allowed groups
            if request.user.groups.filter(name__in=allowed_groups).exists():
                return view_func(request, *args, **kwargs)

            # 3. Otherwise, deny access
            return HttpResponseForbidden("Permission denied")
        return wrapper
    return decorator


# ----- Admin -----
class IsAdmin(permissions.BasePermission):
    """
    Allows access only to users in the 'Admin' group.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Admin").exists()
        )

# ----- Supervisor -----
class IsSupervisor(permissions.BasePermission):
    """
    Allows access only to users in the 'Supervisor' group.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Supervisor").exists()
        )

# ----- Staff -----
class IsStaff(permissions.BasePermission):
    """
    Allows access only to users in the 'Staff' group.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Staff").exists()
        )
