from rest_framework import permissions

# ----- Admin -----
class Is_admin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Admin").exists()
        )

# ----- Supervisor -----
class IsSupervisor(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Supervisor").exists()
        )

# ----- Staff -----
class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Staff").exists()
        )

# ----- Combined: Admin OR Supervisor -----
class IsAdminOrSupervisor(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.groups.filter(name="Admin").exists()
                or request.user.groups.filter(name="Supervisor").exists()
            )
        )

# ----- Combined: Staff OR Supervisor -----
class IsStaffOrSupervisor(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.groups.filter(name="Staff").exists()
                or request.user.groups.filter(name="Supervisor").exists()
            )
        )
