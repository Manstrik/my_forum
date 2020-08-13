"""Модели приложения profiles."""

from django.db import models

from profiles.utils import get_avatar_upload_path


class Profile(models.Model):
    """Модель профиля пользователя."""

    user = models.OneToOneField('auth.User', models.CASCADE, verbose_name='Пользователь')

    avatar = models.ImageField('Аватар профиля', upload_to=get_avatar_upload_path, blank=True, null=True)
    date_of_birth = models.DateField('Дата рождения', blank=True, null=True)
    middle_name = models.CharField('Отчество', max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        db_table = 'profiles'

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
