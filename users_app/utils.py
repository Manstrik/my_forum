"""Файл дополнительных утилит приложения users_app."""
import os


def get_avatar_upload_path(instance, filename):
    """
    Функция для получения уникальной папки для аватара профиля.

    :param instance: объект профиля
    :param filename: имя файла
    :return: путь к файлу
    """
    return os.path.join('avatars', instance.user.username, filename)
