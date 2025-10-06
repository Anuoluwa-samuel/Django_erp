from django.urls import path
from .views import dashboard_view, login_view, logout_view, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),(template_name) name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

