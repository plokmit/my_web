from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from users.forms import UserCreationForm

from .models import User


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)


def get_balance(request):
    template_name = 'balance/balance.html'
    if request.user.is_authenticated:
        username = request.user.username
        row = User.objects.get(username=username)
        balance = row.payment.balance
        return render(request, template_name, {'balance': balance})
    else:
        return redirect('login')
