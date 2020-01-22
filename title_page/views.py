"""Представления для приложения title_page."""

from django.views.generic import ListView

from title_page.models import Post


class IndexView(ListView):
    """Класс-представление основной страницы приложения title_page."""

    template_name = 'title_page/index.html'
    model = Post
    context_object_name = 'posts'
