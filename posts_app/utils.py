"""Файл дополнительных утилит приложения posts_app."""

import os

TRASH_KEYS = ['csrfmiddlewaretoken']


def multipart_to_dict(multi_part_data):
    """
    Функция конвертации объекта вида multi-part в словарь.

    :param multi_part_data: объект для конвертации
    :return: преобразованный словарь
    """
    data = {key: value for key, value in multi_part_data.items() if key not in TRASH_KEYS}

    return data


def get_post_image_upload_path(instance, filename):
    """
    Функция для получения уникальной папки для картинки с постом.

    :param instance: объект поста
    :param filename: имя файла
    :return: путь к файлу
    """
    return os.path.join('posts', instance.created_by.username, filename)
