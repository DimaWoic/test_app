from .models import Article
import requests
import time
from django.db.utils import IntegrityError
from test_app.habroparser.habr_parser import HabroParser


def test_model():
    print('Проверка добавления в поле title модели Article не уникальных записей. ВНИМАНИЕ! ВСЕ СУЩЕСТВУЮЩИЕ ЗАПИСИ '
          'БУДУТ УДАЛЕНЫ')
    time.sleep(3)
    try:
        Article.objects.all().delete()
        Article.objects.create(title='тест', text='тест ' * 50, source='http://127.0.0.1:8000/articles/')
        Article.objects.create(title='тест', text='тест ' * 50, source='http://127.0.0.1:8000/articles/')
        print('Fail')
    except IntegrityError:
        print('ОК')
        Article.objects.all().delete()


def test_api_content():
    print('Проверка приложения с данными')
    time.sleep(3)
    print('Наполняю контентом')
    try:
        parser = HabroParser(url='https://habr.com/ru/')
        parser.content_parser()
    except IntegrityError:
        pass
    print('Проверка наличия соединения с API')
    time.sleep(3)
    try:
        r = requests.get('http://127.0.0.1:8000/articles/')
        if r.status_code == 200:
            print("ОК")
        else:
            print('Fail')
    except Exception as error:
        print(error)

    print('Проверка наличия соединения с отдельно взятой статьёй')
    time.sleep(3)
    try:
        id = requests.get('http://127.0.0.1:8000/articles/').json()['results'][0]['id']
        r = requests.get('http://127.0.0.1:8000/articles/' + str(id))
        if r.status_code == 200:
            print("ОК")
        else:
            print('Fail')
    except Exception as error:
        print(error)

    print('Проверка пагинации')
    time.sleep(3)
    try:
        r = requests.get('http://127.0.0.1:8000/articles/')
        if r.status_code == 200:
            if r.json()['next'] != None:
                print('Переход на следующую страницу ', r.json()['next'])
                time.sleep(3)
                n = requests.get(r.json()['next'])
                if n.status_code == 200:
                    print('OK')
                    time.sleep(3)
                    print('Переход на предыдущую страницу ', n.json()['previous'])
                    time.sleep(3)
                    p = requests.get(n.json()['previous'])
                    if p.status_code == 200:
                        print('OK')
                    else:
                        print('Fail')
                else:
                    print('Fail, Нет пагинации добавьте минимум 12 статей')
            else:
                print('Fail')

        else:
            print('Fail')
    except Exception as error:
        print(error)


def test_api_no_content():
    print('Проверка приложения без контента, база данных будет очищена')
    Article.objects.all().delete()
    time.sleep(3)
    print('Проверка наличия соединения с API')
    time.sleep(3)
    try:
        r = requests.get('http://127.0.0.1:8000/articles/')
        if r.status_code == 200:
            print("ОК")
        else:
            print('Fail')
    except Exception as error:
        print(error)

    print('Проверка наличия соединения с отдельно взятой статьёй')
    time.sleep(3)
    try:
        r = requests.get('http://127.0.0.1:8000/articles/1/')
        if r.status_code == 200:
            print("ОК")
        else:
            print('Fail')
    except Exception as error:
        print(error)

    print('Проверка пагинации')
    time.sleep(3)
    try:
        r = requests.get('http://127.0.0.1:8000/articles/')
        if r.status_code == 200:
            if r.json()['next'] != None:
                print('Переход на следующую страницу ', r.json()['next'])
                time.sleep(3)
                n = requests.get(r.json()['next'])
                if n.status_code == 200:
                    print('OK')
                    time.sleep(3)
                    print('Переход на предыдущую страницу ', n.json()['previous'])
                    time.sleep(3)
                    p = requests.get(n.json()['previous'])
                    if p.status_code == 200:
                        print('OK')
                    else:
                        print('Fail')
                else:
                    print('Fail, Нет пагинации добавьте минимум 12 статей')
            else:
                print('Fail')

        else:
            print('Fail')
    except Exception as error:
        print(error)


#test_model()
test_api_content()
#test_api_no_content()
