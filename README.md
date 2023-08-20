# django-orm-watching-storage
Данный проект создан в рамках урока Урок 2. Разворачиваем сайт локально

С помощью этого проекта можно локально развернуть сайт по проекту django-orm-watching-storage

## Требуемые пакеты
django==3.2.*

psycopg2-binary==2.9.*

python-dotenv~=1.0.0

environs~=9.5.0

## Инструкция по установке и запуску
Для примера мы клонируем репозиторий в D:\django-orm, можно выбрать другую директорию. 
Инструкция приведена для Windows
```
$ git clone https://github.com/Alxplcn/django-orm-watching-storage D:\django-orm
$ D:
$ cd D:\django-orm
$ pip install -r requirements.txt
$ python manage.py runserver 0.0.0.0:8000
```
Требуется, чтобы в папке D:\django-orm был файл .env с параметрами бд

В случае успеха пользователь сможет открыть сайт в браузере по адресу 127.0.0.1:8000

## Контакты
Автор -- https://dvmn.org/user/id101939300/
