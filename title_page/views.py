"""Представления для приложения title_page."""

from django.contrib.auth.models import User
from django.views.generic import ListView


class IndexView(ListView):
    """Класс-представление основной страницы приложения title_page."""

    template_name = 'title_page/index.html'
    model = User
    context_object_name = 'users'
