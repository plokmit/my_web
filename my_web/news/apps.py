from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'


'''class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals'''