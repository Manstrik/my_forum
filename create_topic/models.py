"""Модели приложения create_topic."""

from django.db import models



class CreatePost(models.Model):
    """Модель нового поста на форуме."""
    post_user_name = models.CharField(verbose_name='Имя пользователя', default='Не задано имя', max_length=128)
    post_name = models.CharField(verbose_name='Тема поста', default='Не задано имя поста', max_length=128)
    post_text = models.TextField(verbose_name='Текст поста', default='Текст не введён')
    post_time = models.DateTimeField(verbose_name='Дата и время поста', auto_now_add=True)
