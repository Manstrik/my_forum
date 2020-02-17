"""Файл маршрутов приложения posts_app."""

from django.urls import path
from django.views.generic import TemplateView

from posts_app.views import create_post, PostDetail, PostList

app_name = 'posts_app'

urlpatterns = [
    # Главная страница приложения со списком постов
    path(r'', PostList.as_view(), name='post-list'),

    # Страница с детальной информацией о посте
    path(r'<int:pk>/', PostDetail.as_view(), name='post-detail'),

    # Страница с формой для создания нвого поста
    path(r'new-post/', TemplateView.as_view(template_name='post_create.html'), name='new-post'),

    # API-функция для создания поста
    path('create/', create_post, name='create')
]
