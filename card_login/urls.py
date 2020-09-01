from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth_otp/', views.auth_otp, name='auth_otp'),
]
