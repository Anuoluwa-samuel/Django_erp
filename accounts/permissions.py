from django.http import HttpResponseForbidden

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
