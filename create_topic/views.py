"""Представления для приложения create_topic."""

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import CreatePost


class Index(ListView):
    """Класс-представление основной страницы приложения create_topic."""

    template_name = 'index.html'
    # Ты передавал неправильную модель в шаблон (скопировал ранее у меня видимо)
    # model = User
    model = CreatePost
    # Аналогично с именем, под которым тебе передается в шаблон
    # context_object_name = 'users'
    context_object_name = 'posts'


def create_post(request):
    """
    Функция для создания поста.

    :param request: обхект запроса
    """
    text_field = None
    text_post_name = None
    if request.method == 'POST':  # если запрос пост, то
        if 'text_field' in request.POST:
            text_field = request.POST['text_field']  # текст поста
            text_post_name = request.POST['post_name']  # название поста
    if request.method == 'GET':  # присваиваем значение в строке браузера/переменной
        text_field = request.GET['text_field']  # текст поста
        text_post_name = request.GET['post_name']  # название поста
    if text_field and text_post_name is not None:
        create_text = CreatePost(post_text=str(text_field),  # сохраняем в базу
                                 post_name=str(text_post_name))
        create_text.save()
    return HttpResponse('Добавлено!')


def loading_postdb(request):
    """
    Здесь должен быть комментарий.

    :param request:
    :return:
    """
    posts = CreatePost.objects.all()  # загружаем все данные из БД
    return render(request, 'index.html', locals())  # передаём их в html


class SearchPostsInDB:
    """Класс для поиска постов в БД."""

    def __init__(self):
        """Метод-конструктор класса."""
        self.query = None

    def get_text(self, request):
        """Метод для получения значения для фильтрации."""
        self.query = request.GET['search_posts']
        return self.query

    def searching_in_db(self):
        """Метод для поиска в БД."""
        search_query = SearchQuery(self.get_text)
        search_vector = SearchVector(self.get_text)
        search_rank = SearchRank(search_vector, search_query)
        result_searching = CreatePost.objects.annotate(rank=search_rank).order_by('-rank').value_list('text_post_name',
                                                                                                      'text_field')
        return result_searching
