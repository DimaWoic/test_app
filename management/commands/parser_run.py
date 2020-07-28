from django.core.management.base import BaseCommand, CommandError
from test_app.habroparser.habr_parser import HabroParser


class Command(BaseCommand):
    def handle(self, *args, **options):

        parser = HabroParser(url='https://habr.com/ru/')
        parser.content_parser()