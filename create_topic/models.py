"""Модели приложения create_topic."""

from django.db import models


class CreatePost(models.Model):
    """Модель нового поста на форуме."""

    new_post = models.TextField('Текст поста', default=None)
