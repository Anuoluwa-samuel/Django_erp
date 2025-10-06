from django.urls import path
from .views import dashboard, login, logout, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard, name='dashboard'),


]

