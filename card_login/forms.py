from django.contrib.auth.models import User
from django import forms
from .models import Record


class CardLoginForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['id']
