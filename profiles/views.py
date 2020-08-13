"""Файл с представлениями приложение profiles."""

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import redirect

from lib.utils import multipart_to_dict


def logout(request):
    """Функция для разлогинивания пользователя."""
    response = redirect('posts:post_list')

    if request.method == 'GET':
        return response

    if request.user.is_authenticated:
        django_logout(request)

    return response


def login(request):
    """Функция для входа пользователей пользователя."""
    response = redirect('posts:post_list')

    if request.method == 'GET':
        return response

    data = multipart_to_dict(request.POST)

    user = authenticate(request, **data)
    if user:
        django_login(request, user)

    return response
