from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Record
from .forms import CardLoginForm, OtpForm
from .otp import send_otp


# Create your views here.
def home(request):
    if request.method == 'POST':
        login_form = CardLoginForm(request.POST)
        card_number = request.POST['id']
        request.session['CARD_NUMBER'] = card_number
        record = Record.objects.filter(id=card_number).first()
        print(record)
        if record is not None:
            return redirect(f'/auth_otp')
        else:
            return redirect('/')
    else:
        login_form = CardLoginForm()
        context = {'form': login_form}
        return render(request, 'login/home.html', context)


def auth_otp(request):
    if request.method == 'GET':
        card_number = request.session['CARD_NUMBER']
        record = Record.objects.filter(id=card_number).first()
        phone_number = record.mobile_number
        _sid, otp = send_otp(card_number, phone_number)
        request.session['OTP'] = otp
        print(f"otp {otp}")
        otp_form = OtpForm()
        context = {'form': otp_form}
        return render(request, 'login/otp.html', context)
    elif request.method == 'POST':
        form_otp = request.POST.get('otp')
        otp = request.session.get('OTP')
        print(f"form {form_otp} otp {otp}")
        if form_otp == otp:
            return redirect('/warn_face')
        else:
            return redirect('/')

    # return HttpResponse(
    # f'<h1>Hello There my phone_number is {phone_number}</h1>')
