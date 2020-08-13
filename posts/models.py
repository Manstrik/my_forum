"""Модели приложения posts."""

from django.db import models

from posts.utils import get_post_image_upload_path


class Post(models.Model):
    """Модель поста на форуме."""

    title = models.CharField('Заголовок', max_length=256)
    summary = models.TextField('Текст на предпросмотре')
    content = models.TextField('Текст поста')
    added_date = models.DateTimeField('Дата добавления поста', auto_now_add=True)
    created_by = models.ForeignKey('auth.User', models.CASCADE, verbose_name='Кто добавил пост')
    preview_image = models.ImageField('Картинка на посте', upload_to=get_post_image_upload_path, blank=True, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'posts'

    def __str__(self):
        return self.title
