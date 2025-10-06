from django.contrib import admin
from django.urls import path, include
from dashboard import views as user_view
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')), 
    path('inventory/', include('inventory.urls')),
    path('purchases/', include('purchases.urls')),
    path('', lambda request: redirect('login'), name='home'),

    path('register/', user_view.tr, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]

if getattr(settings, "ENVIRONMENT", "development") == "development":
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
