"""Файл сигналов для приложения users_app."""

import os

from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

from lib.utils import delete_empty_dirs
from users_app.models import Profile


@receiver(post_delete, sender=Profile)
def delete_avatar(sender, instance: Profile, **kwargs):
    """
    Сигнал для удаления файла из файловой системы.

    :param sender: отправитель сигнала
    :param instance: объект модели
    :param kwargs: дополнительные параметры
    """
    instance.avatar.delete(False)
    delete_empty_dirs(os.path.join(settings.BASE_DIR, 'media'))
