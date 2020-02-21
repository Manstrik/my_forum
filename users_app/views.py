"""Файл с представлениями приложение users_app."""

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import redirect

from lib.utils import multipart_to_dict


def logout(request):
    """Функция для разлогинивания пользователя."""
    if request.user.is_authenticated:
        django_logout(request)

    return redirect('posts_app:post_list')


def login(request):
    """Функция для входа пользователей пользователя."""
    data = multipart_to_dict(request.POST)

    user = authenticate(request, **data)
    if user:
        django_login(request, user)

    return redirect('posts_app:post_list')
