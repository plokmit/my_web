from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"), #обращаемся без выполнения, поэтому без скобок
    path('about', views.about, name = "about")
]