"""Конфигурационный файл приложения profiles."""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Класс-конфиг для приложения profiles."""

    name = 'profiles'
    verbose_name = 'Данные о пользователях форума'

    def ready(self):
        """Функция, выполняемая после запуска приложения. Делает импорт сигналов для моделей."""
        # noinspection PyUnresolvedReferences
        from profiles import signals  # noqa F401
