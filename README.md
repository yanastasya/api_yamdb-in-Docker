Учебный проект в рамках курса Backend Python-разработчик от Яндекс.Практикум. Упаковка проекта в контейнеры.

[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

# Проект YaMDb в контейнерах.
В данном репозитории проект [API_yamDB](https://github.com/yanastasya/api_yamdb) упакован в контейнеры nginx, db (PostegresSQL) и web (само приложение). Данная инфраструктура позволяет развернуть проект на вашем ПК без необходимости разворота venv, установки зависимостей, базы данных на вашем ПК. 

# Для запуска:
- скачать репозиторий
- К проекту подключена БД PostgresSQL. Для её корректной работы необходимо в папке infra/ создать файл .env и заполнить его по образцу ниже:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=qwerty # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

- Для запуска в терминале выполнить команду ``` docker-compose up -d --build ``` из дериктории, где находится файл docker-compose.yaml

- После сбора образов и запуска контейнеров необходимо зайти в контейнер web, выполнить миграции, собрать статику, создать суперпользователя и загрузить данные в БД из файлов CSV. Для этого последовательно выполнить команды:
- Выполнить миграции:
``` 
docker-compose exec web bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --no-input

python manage.py load_category_data
python manage.py load_genre_data
python manage.py load_users_data
python manage.py load_title_data
python manage.py load_genre_title_data
python manage.py load_rewiews_data
python manage.py load_comments_data
```
