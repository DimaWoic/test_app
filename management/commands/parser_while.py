from django.core.management.base import BaseCommand, CommandError
from test_app.habroparser.habr_parser import HabroParser
import time


class Command(BaseCommand):
    """Базовый класс для реализации собственных комманд пользователя.
        Обязательным методом класса является:
            def handle(self, *args, **options):
                ...Ваш код...
        Здесь служит для запуска парсера(который будет собирать данные раз 24 часа)
         из консоли следующей командой:
        python manage.py parser_while.
        """

    def handle(self, *args, **options):
        while True:
            parser = HabroParser(url='https://habr.com/ru/')
            parser.content_parser()
            time.sleep(86400)