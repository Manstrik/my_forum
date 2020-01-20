FROM python:3-slim-stretch

WORKDIR /app

EXPOSE 8000

RUN pip install --upgrade pip \
 && pip install gunicorn

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT python manage.py migrate \
        && python manage.py collectstatic --noinput \
        && gunicorn my_forum.wsgi -b 0.0.0.0 --access-logfile - --log-file -
