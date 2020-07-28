from django.core.management.base import BaseCommand, CommandError
from test_app.habroparser.habr_parser import HabroParser
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            parser = HabroParser(url='https://habr.com/ru/')
            parser.content_parser()
            time.sleep(86400)