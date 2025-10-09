from django.urls import path
from .views import dashboard_view, login_view, logout_view, register, terms_of_service, privacy_policy, 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('terms-of-service/', terms_of_service, name='terms_of_service'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('cookies-policy/', cookies_policy, name='cookies_policy'),
]

