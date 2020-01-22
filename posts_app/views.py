"""Представления для приложения posts_app."""
from django.views.generic import DetailView, ListView

from posts_app.models import Post


class PostList(ListView):
    """Класс-представление страницы с постами приложения posts_app."""

    template_name = 'posts_app/post_list.html'
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    """Класс-представление страницы с детальной информацией о посте приложения posts_app."""

    template_name = 'posts_app/post_detail.html'
    model = Post
    context_object_name = 'post'
