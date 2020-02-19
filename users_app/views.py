"""Файл с представлениями приложение users_app."""

from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect


def logout(request):
    """Функция для разлогинивания пользователя."""
    if request.user.is_authenticated:
        django_logout(request)

    return redirect('posts_app:post_list')
