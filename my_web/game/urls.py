from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='game'),
    path('new_game/', views.one_game, name='new_game')
]
