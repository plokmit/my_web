from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.all
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    fields = ['title', 'anons', 'full_text']

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete-news.html'
    success_url = '/news'

def create(request):
    form = ArticlesForm()
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'
    data = {
        'form':form,
    }
    return render(request, 'news/create.html', data)

