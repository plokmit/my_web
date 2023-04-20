from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='game'),
    path('new_game/', views.new_game, name='new_game'),
    path('new_game/result/', views.result, name='result')
]
