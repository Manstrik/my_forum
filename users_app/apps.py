"""Конфигурационный файл приложения users_app."""

from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    """Класс-конфиг для приложения users_app."""

    name = 'users_app'
    verbose_name = 'Данные о пользователях форума'
