from random import randint
from django.shortcuts import render, redirect
from users.models import User, Payment

choice_bet = 0
def start(request):
    template_name = 'game.html'
    return render(request, template_name)
def new_game(request):
    template_name = 'choice.html'

    global choice_bet
    choice_bet = int(request.POST.get('choice_bet'))

    data = {
        'choice_bet': choice_bet
    }
    return render(request, template_name, data)

def result(request):
    template_name = 'result.html'
    global choice_bet

    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    coefficients = {
        1: 35,
        2: 17,
        3: 11,
        4: 8,
        5: 1,
        6: 1
    }

    username = request.user.username
    row = User.objects.get(username=username)
    number = request.POST.getlist("number")
    print(number)
    number = [int(i) for i in number]
    bet = int(request.POST.get('bet'))
    print(number)

    if 0 < choice_bet < 5:
        choice_bet = len(set(number))
    elif choice_bet == 5:
        if 1 in number:
            number = red
        if 2 in number:
            number = [i for i in range(36) if i not in red]

    elif choice_bet == 6:
        if 1 in number:
            number = [_ for _ in range(1, 36, 2)]
        if 2 in number:
            number = [_ for _ in range(2, 37, 2)]

    if bet > row.payment.balance:
        return redirect('game')
    res_of_number = randint(0, 36)
    res_of_number = 5

    if res_of_number in red:
        color = 'красное'
    else:
        color = 'черное'

    if request.user.is_authenticated:
        print(choice_bet)
        if res_of_number in number:
            message = 'Поздравляем! Вы выиграли! '
            row.payment.balance += bet*coefficients[choice_bet]

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
        'bet': bet,
    }

    return render(request, template_name, data)
