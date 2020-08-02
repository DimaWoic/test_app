#####Руководство по установке и настройки RESTful приложения-агрегатора статей с хабр

   Для установки и тестирования приложения на Linux-подобных системах выполните установку следующих пакетов:
1. Установите виртуальную среду vertualenv, c правами администратора в терминале введите следующую команду:
    
    pip3 install vertualenv
    
2. Создайте папку в /home/User/, где User - имя папки пользователя системы и перейдите в неё:
    
    mkdir test_api
    
    cd test_api
    
3. Создайте виртуальную среду с Python 3.8 следующей командой и активируйте её:
    
    virtualenv -p python3.8 venv
    
    source venv/bin/activate
    
4. Установите пакеты командой:
    
    pip install django==3.0.8 djangorestframework requests bs4

5. Создайте проект django командой:

    django-admin startproject testproject
   
   Будет создана следующая структура папок:
   
       test_api|
               |testproject|
               |            |testproject|
               |            |           |__init__.py
               |            |           |asgi.py
               |            |           |settings.py
               |            |           |urls.py
               |            |           |wsgi.py
               |            |manage.py
               |
               |venv
6. Перейдите в папку testproject:

    cd testproject
    
7. Скачайте из репозитория GitHub файлы приложения:
    
    git clone https://github.com/DimaWoic/test_app.git

8. Будет создана следующая структура папок:

        test_api|
                |testproject|
                |           |testproject|
                |           |           |__init__.py
                |           |           |asgi.py
                |           |           |settings.py
                |           |           |urls.py
                |           |           |wsgi.py
                |           |
                |           |test_app |
                |           |         |habroparser
                |           |         |management
                |           |         |migrations
                |           |         |__init__.py
                |           |         |admin.py
                |           |         |apps.py
                |           |         |models.py
                |           |         |README.md
                |           |         |serializers.py
                |           |         |tests.py
                |           |         |urls.py
                |           |         |views.py
                |           |         
                |           |
                |           |manage.py
                |venv

9. Введите команду:
    
    nano testproject/settings.py
    
    И внесите в следующие секции изменения:
    
        INSTALLED_APPS = [
            ...
            ...
            'test_app',
            'rest_framework',
        ]

        LANGUAGE_CODE = 'ru'

        TIME_ZONE = 'Europe/Moscow'
        
        Добавьте следующую секцию:

        LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {
                'file': {
                    'level': 'ERROR',
                    'class': 'logging.FileHandler',
                    'filename': os.path.join(BASE_DIR, 'django.log'),
                },
            },
            'loggers': {
                'django': {
                    'handlers': ['file'],
                    'level': 'ERROR',
                    'propagate': True,
                },
                'django.request': {
                    'handlers': ['file'],
                    'level': 'ERROR',
                    'propagate': True,
                }
            }
        }

10. Введите команду:
    
    nano testproject/urls.py
    
    И внесите следующие изменения:
    
        from django.contrib import admin
        from django.urls import path, include
    
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('test_app.urls')),
        ]
        
11. Для создания миграций, введите команды:

    python manage.py check test_app - производит проверку приложения
    
    python manage.py makemigrations test_app
    
    python manage.py migrate test_app
    
    Будут созданы таблицы в базе данных, в данном случае для тестирования была выбрана в качестве 
    хранилища db.sqlite3(файл базы данных будет создан в папке уровня проекта при выполнении
    миграции)
    
Теперь можно запустить сервер разработки следующей командой:

    python manage.py runserver
    
Будет запущен сервер разработки по адресу  http://127.0.0.1:8000/

При попытке перехода по вышеукзанному адресу будет выдана ошибка 404

Для доступа к API приложения необходимо в адресную строку браузера передать следующий адрес:

    http://127.0.0.1:8000/articles/
    
Будет выведен пустой листинг статей. Для наполнения базы данных контентом и вывода в API
необходимо выполнить следующую команду:
    
    python manage.py parser_run

Данная команда будет запускать парсер единажды, команда:
    
    python manage.py parser_while - запустит парсер в цикл и будет производить опрос раз в сутки

Теперь можно повтарить ввод в адресную строку адреса http://127.0.0.1:8000/articles/, будет выведен
листинг статей с следующими полями id, title, text.

Для доступа к отдельной статье вводим в браузере http://127.0.0.1:8000/articles/1, где 1 - это id
статьи. Будет выведен листинг отдельной статьи с полями: title, text, source

Для изменения количества выводимых статей можно передать http://127.0.0.1:8000/articles/?page_size=5
будет выведено 5 элементов

Переход на последнюю страницу http://127.0.0.1:8000/articles/?page=end

Приложением предусмотрено тестирование, вызвается командой:

    python manage.py test

Первый тест выполняет проверку поведения модели при попытке записи в неё одинаковых значений, если возбуждается 
исключение IntegrityError тест пройден отобразится OK
Далее тестирование при наличии контента

1. Производится проверка доступности API по адресу: 'http://127.0.0.1:8000/articles/', если тест пройден будет 
выведено сообщение OK, в противном случае FAIL. 
2. Попытка доступности отдельно взятой статьи, если тест пройден будет выведено сообщение OK, в противном случае FAIL.
3. Проверка пагинации, переход на страницу вперёд и назад, если тест провален будет выведено соответствующее сообщение.

Следующий тест выполняет тестирование API без контента:

1. Производится тестирование доступности API по адресу: 'http://127.0.0.1:8000/articles/', если тест пройден будет 
выведено сообщение OK, в противном случае FAIL. 
2. Если не одной статьи нет тест выведет OK, в противном случае нужно удалить все записи из базы данных и повторить
попытку.
3. Тест пагинации не действителен, если предыдущий тест провален

Внимание!!! для вывода описания классов содержащимся во views, добавлена
функция documentation().