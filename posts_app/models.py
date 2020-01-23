"""Модели приложения posts_app."""

from django.contrib.auth.models import User
from django.db import models

from posts_app.utils import get_post_image_upload_path


class Post(models.Model):
    """Модель поста на форуме."""

    title = models.CharField('Заголовок', max_length=256)
    summary = models.TextField('Текст на предпросмотре')
    content = models.TextField('Текст поста')
    added_date = models.DateTimeField('Дата добавления поста', auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил пост')
    preview_image = models.ImageField('Картинка на посте', upload_to=get_post_image_upload_path, blank=True, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        # Имя таблицы для этой модели
        db_table = 'Ууууу сука, таблица'

    def __str__(self):
        return self.title
