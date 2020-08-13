"""my_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    # Админка сайта
    path('admin/', admin.site.urls),
    # Раздел редиректа
    path('', RedirectView.as_view(url='posts/'), name='home'),
    # Приложение posts
    path('posts/', include('posts.urls', namespace='posts')),
    # Приложение profiles
    path('profiles/', include('profiles.urls', namespace='profiles')),
    # Создание темы на форуме
    path('create_topic/', include('create_topic.urls', namespace='create_topic')),
    # Показ созданных тем
]

handler404 = 'my_forum.views.handler404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
