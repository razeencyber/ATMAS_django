from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Record
from .forms import CardLoginForm


# Create your views here.
def home(request):

    if request.method == 'POST':
        login_form = CardLoginForm(request.POST)
        card_number = request.POST['id']
        record = Record.objects.get(id=card_number)
        if record is not None:
            return redirect('/admin')
        else:
            return redirect('/')
    else:
        login_form = CardLoginForm()
        context = {'form': login_form}
        return render(request, 'login/home.html', context)
