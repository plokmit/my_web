from django.shortcuts import render

def index(request):

    return render(request, 'main/index.html')
    '''что показывать пользователю; big pages; в кач-ве второго
    #в кач-ве второго аргумента название шаблона
    создаем в приложении папку templates, в ней папку с названием приложения (templates создается (и потом объединяется в одну) в каждом 
    приложении  и нам надо избежать конфликта имен)
    Когда обращаемся к шаблону, представляем что уже находимся в папке templates и прописываем относительный путь

def about(request):
    return HttpResponse('<h4>хуй</h4>') #не выводим большие страницы'''

def about(request):
    return render(request, 'main/about.html')