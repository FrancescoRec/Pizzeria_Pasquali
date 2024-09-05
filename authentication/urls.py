from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Custom register view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Django built-in login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Django built-in logout view
    path('dashboard/', views.dashboard, name='dashboard'),  # Redirect after login
]