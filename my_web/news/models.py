from django.db import models

# Create your models here.

class Articles(models.Model): # создаем поля, которык будут полями в таблице
    # в зависимости от типа поля вводим разные символы
    title = models.CharField('Название', max_length=50, default='Неизвестное название')
    anons = models.CharField('Анонс', max_length=250, default='Пустое описание') #максимум символов в charfield - 250 символов
    full_text = models.TextField('Статья')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'