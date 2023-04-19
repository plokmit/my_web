from random import randint
from django.shortcuts import render, redirect
from users.models import User, Payment

def start(request):
    template_name = 'game.html'
    return render(request, template_name)
def one_game(request):
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    template_name = 'result.html'
    number = int(request.POST.get('number'))
    bet = int(request.POST.get('bet'))
    username = request.user.username
    row = User.objects.get(username=username)
    if bet > row.payment.balance:
        return redirect('game')
    res_of_number = randint(0, 36)
    res_of_number = 5
    if number in red:
        color = 'красное'
    else:
        color = 'черное'
    if request.user.is_authenticated:

        print(row.payment.balance)
        if number == res_of_number:
            message = 'Поздравляем! Вы выиграли! '
            row.payment.balance += bet*35
        else:
            message = 'Сожалеем, вы проиграли'
            row.payment.balance -= bet
        row.payment.save()
        balance = row.payment.balance

    data = {
        'number': number,
        'res_of_number': res_of_number,
        'color': color,
        'message': message,
        'balance': balance,
    }
    return render(request, template_name, data)
