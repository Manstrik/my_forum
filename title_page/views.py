"""Представления для приложения title_page."""

from django.contrib.auth.models import User
from django.views.generic import ListView


class IndexView(ListView):
    """Класс-представление основной страницы приложения title_page."""

    template_name = 'title_page/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        """
        Контекст, передаваемый в шаблон.

        :return: список всех пользователей
        """
        return User.objects.all()
