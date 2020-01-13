"""Общие представления для всего проекта."""

from django.shortcuts import render


def handler404(request, exception):
    """
    Кастомная страница обработки ошибки 404.

    :param request: объект запроса
    :param exception: объект ошибки
    :return: отрендеренный шаблон
    """
    return render(request, 'error_pages/404.html', context={'exception': exception})
