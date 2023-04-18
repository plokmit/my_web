from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


class User(AbstractUser):
    pass


class Payment(models.Model):
    user_balance = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=1000, verbose_name='balance')

@receiver(post_save, sender=User)
def create_balance(sender, instance, created, **kwargs):
    print('post-save')
    if created:
        Payment.objects.create(user_balance=instance)
    else:
        return redirect ('home')
