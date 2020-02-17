"""Конфигурационный файл приложения posts_app."""

from django.apps import AppConfig


class PostsAppConfig(AppConfig):
    """Класс-конфиг для приложения posts_app."""

    name = 'posts_app'
    verbose_name = 'Данные о постах на форуме'

    def ready(self):
        """Функция, выполняемая после запуска приложения. Делает импорт сигналов для моделей."""
        # noinspection PyUnresolvedReferences
        from posts_app import signals  # noqa F401
