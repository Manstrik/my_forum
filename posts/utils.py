"""Файл дополнительных утилит приложения posts."""

import os


def get_post_image_upload_path(instance, filename):
    """
    Функция для получения уникальной папки для картинки с постом.

    :param instance: объект поста
    :param filename: имя файла
    :return: путь к файлу
    """
    return os.path.join('posts', instance.author.username, filename)
