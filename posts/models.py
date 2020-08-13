"""Модели приложения posts."""

from django.db import models

from posts.utils import get_post_image_upload_path


class Post(models.Model):
    """Модель поста на форуме."""

    title = models.CharField('Заголовок', max_length=256)
    summary = models.TextField('Текст на предпросмотре')
    content = models.TextField('Текст поста')
    published = models.DateTimeField('Дата публикации поста', auto_now_add=True)
    author = models.ForeignKey('auth.User', models.CASCADE, verbose_name='Автор поста', related_name='posts')
    preview_image = models.ImageField('Картинка на посте', upload_to=get_post_image_upload_path, blank=True, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'posts'

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Модель комментария к постую"""

    text = models.TextField('Текст комментария', blank=True, null=True)
    author = models.ForeignKey('auth.User', models.CASCADE, verbose_name='Автор комментария', related_name='comments')
    published = models.DateTimeField('Дата публикации', auto_now_add=True)
    to_post = models.ForeignKey('Post', models.CASCADE, verbose_name='Пост', related_name='comments')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        db_table = 'comments'
