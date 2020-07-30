from django.core.management.base import BaseCommand
from test_app.habroparser.habr_parser import HabroParser


class Command(BaseCommand):
    """Базовый класс для реализации собственных комманд пользователя.
    Обязательным методом класса является:
        def handle(self, *args, **options):
            ...Ваш код...
    Здесь служит для запуска парсера(который будет собирать данные единажды) из консоли следующей командой:
    python manage.py parser_run.
    """

    def handle(self, *args, **options):

        parser = HabroParser(url='https://habr.com/ru/')
        parser.content_parser()