FROM python:3.7-slim-stretch

WORKDIR /app

EXPOSE 8000

RUN pip install --upgrade pip \
 && pip install gunicorn

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT mkdir -p pids logs \
        && rm -rf nginx \
        && python manage.py migrate \
        && python manage.py collectstatic --noinput \
        && gunicorn my_forum.wsgi -b 0.0.0.0:8000 -p pids/gunicorn.pid --access-logfile logs/gunicorn-access.log --log-file logs/gunicorn.log
