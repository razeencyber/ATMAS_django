from django.shortcuts import render, redirect
# from django imp
from card_login.models import Record
# Create your views here.


def demo(request):
    # card_number = request.session.get('CARD_NUMBER')
    # user = Record.objects.filter(id=card_number).first()
    user = Record.objects.filter(id=123).first()
    if user is None:
        return redirect('home')
    context = {
        'name': str(user.first_name + " " + user.last_name),
        'money': user.current_balance
    }
    return render(request, 'demo.html', context)
