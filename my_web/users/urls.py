from django.contrib.auth import views
from django.urls import path, include

from users.views import Register
from .views import get_balance

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('get-balance/', get_balance, name='get_balance')
    #path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

