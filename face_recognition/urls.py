from django.urls import path
from . import views

urlpatterns = [
    path('warn_face/', views.warn_face, name='warn_face'),
    path('detectFace/', views.detectFace, name='detectFace'),
]
