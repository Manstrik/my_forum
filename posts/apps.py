"""Конфигурационный файл приложения posts."""

from django.apps import AppConfig


class PostsAppConfig(AppConfig):
    """Класс-конфиг для приложения posts."""

    name = 'posts'
    verbose_name = 'Данные о постах на форуме'

    def ready(self):
        """Функция, выполняемая после запуска приложения. Делает импорт сигналов для моделей."""
        # noinspection PyUnresolvedReferences
        from posts import signals  # noqa F401
