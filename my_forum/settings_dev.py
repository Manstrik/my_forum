"""Файл настройка для dev-режима."""

import os
import platform

try:
    from .pss import pss
    from .pss_db import pss_db
    from .secret_key import secret_key
except ImportError:
    pass

from .settings import BASE_DIR, DATABASES

try:
    SECRET_KEY = secret_key()
except NameError:
    SECRET_KEY = 'test'

DEBUG = True

ALLOWED_HOSTS = ['*']

try:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_forum',
        'USER': 'vladislav',
        'PASSWORD': pss_db(),
        'HOST': '127.0.0.1',
        'PORT': '5432'  # порт/ip должен соответствовать порту, на котором "слушает" СУБД
        # это не настройка Django - это настройка PostreSQL и менять её надо там
    }
except NameError:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_forum',
        'USER': 'vladislav',
        'PASSWORD': 'test',
        'HOST': '127.0.0.1',
        'PORT': '5432'  # порт/ip должен соответствовать порту, на котором "слушает" СУБД
        # это не настройка Django - это настройка PostreSQL и менять её надо там
    }

# Настройки БД для Коли
if (platform.system() == 'Windows' and os.getlogin() == 'Nikolay') \
        or (platform.system() == 'Linux' and os.getlogin() == 'nikolay'):
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
