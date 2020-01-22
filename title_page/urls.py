"""Файл маршрутов приложения title_page."""

from django.urls import path

from title_page.views import PostDetail, PostList

app_name = 'title_page'

urlpatterns = [
    # Главная страница приложения со списком постов
    path('', PostList.as_view(), name='post-list'),
    # Страница с детальной информацией о посте
    path(r'<int:pk>/', PostDetail.as_view(), name='post-detail')
]
