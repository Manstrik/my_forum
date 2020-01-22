"""Модели приложения title_page."""

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Модель поста на форуме."""

    title = models.CharField('Заголовок', max_length=256)
    summary = models.TextField('Текст на предпросмотре')
    content = models.TextField('Текст поста')
    added_date = models.DateTimeField('Дата добавления поста', auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил пост')
