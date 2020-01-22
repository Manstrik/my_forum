"""Представления для приложения title_page."""

from django.views.generic import DetailView, ListView

from title_page.models import Post


class PostList(ListView):
    """Класс-представление страницы с постами приложения title_page."""

    template_name = 'title_page/post_list.html'
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    """Класс-представление страницы с детальной информацией о посте приложения title_page."""

    template_name = 'title_page/post_detail.html'
    model = Post
    context_object_name = 'post'
