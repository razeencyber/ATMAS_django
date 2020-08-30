from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Records
# Create your views here.
def home(request):
    return  render(request, 'login/home.html')

