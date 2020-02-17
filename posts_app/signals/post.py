"""Файл сигналов для приложения posts_app."""

from django.db.models.signals import post_delete
from django.dispatch import receiver

from posts_app.models import Post


@receiver(post_delete, sender=Post)
def delete_preview_image(sender, instance: Post, **kwargs):
    """
    Сигнал для удаления файла из файловой системы.

    :param sender: отправитель сигнала
    :param instance: объект модели
    :param kwargs: дополнительные параметры
    """
    instance.preview_image.delete(False)
