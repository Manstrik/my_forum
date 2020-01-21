"""Представления для приложения create_topic."""

from django.contrib.auth.models import User
from django.views.generic import ListView


class Index(ListView):
    """Класс-представление основной страницы приложения create_topic."""

    template_name = 'create_topic/index.html'
    model = User
    context_object_name = 'users'
