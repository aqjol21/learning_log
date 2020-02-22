"""Defines URL patterns for learning_logs."""
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
  # login page
  path('login/', LoginView.as_view(template_name= 'users/login.html'), name='login'),
  # logout page
  path('logout/', views.logout_view, name='logout'),
  # Registration page
  path('register/', views.register, name='register'),
]