"""Представления для приложения posts_app."""
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from posts_app.models import Post
from posts_app.utils import multipart_to_dict


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


def create_post(request):
    """
    API-функция для создания нового поста.

    :param request: объект запроса
    :return: редирект на страницу с постами
    """
    data = multipart_to_dict(request.POST)

    data['preview_image'] = request.FILES.get('preview_image', None)

    data['created_by'] = request.user

    Post.objects.create(**data)

    return redirect('posts_app:post-list')
