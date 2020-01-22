"""Файл маршрутов приложения title_page."""

from django.urls import path

from title_page.views import PostDetail, PostList

app_name = 'title_page'

urlpatterns = [
    # Главная страница приложения
    path('', PostList.as_view(), name='index'),
    path(r'post/<int:pk>/', PostDetail.as_view(), name='post-detail')
]
