import requests
from bs4 import BeautifulSoup
import logging
from test_app.models import Article


class HabroParser:
    """
    класс HabroParser реализует парсер статей с https://habr.com/ru/,
    для корректной работы необходимы модули: requests, bs4, logging, и модель Django: Article.
    Обязательным аргументом для класса является вышеуказанный url.
    Если аргумент указан не будет, будет вызвано исключение.
    """

    logging.basicConfig(filename='habroparser.log', filemode='a',
                        format='%(filename)s[LINE:%(lineno)d]# '
                               '%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.WARNING)

    def __init__(self, url):
        """
        Метод класса запрашивает c url html-документ и часть страницы содержащей
        статьи хабра.
        """

        self.url = url
        try:
            r = requests.get(url)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                posts_list = soup.find('div', class_='posts_list')
                self.soup = soup
                self.posts_list = posts_list
            else:
                logging.error('Заданный узел не доступен ', r.status_code)

        except requests.exceptions.RequestException as connerr:
            logging.error(connerr)

    def content_parser(self):
        """
        Метод запрашивает пагинацию, формирует список страниц для парсинга, ссылки на статьи
        сохраняет контент в базу данных
        """

        pagination = self.soup.find('ul', id='nav-pagess')
        num_pages = pagination.find_all('li')
        list_pagination_pages = []
        link_list = []
        list_pagination_pages.append('https://habr.com/ru/')
        for nums in num_pages:
            num = int(nums.text)
            if num != 1:
                list_pagination_pages.append('https://habr.com/ru/page' + str(num) + '/')
        for url_pages in list_pagination_pages:
            r = requests.get(url_pages)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                posts_list = soup.find('div', class_='posts_list')
                a_tag = posts_list.find_all('a', class_='post__title_link')
                for l in a_tag:
                    link = l.get('href')
                    link_list.append(link)
            else:
                logging.error('Заданный узел не доступен ', r.status_code)

        try:
            for link in link_list:
                r = requests.get(link)
                if r.status_code == 200:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    title = soup.find('span', class_='post__title-text').text
                    text = soup.find('div', id='post-content-body').text
                    article = Article()
                    article.title = title
                    article.text = text.replace('\r', ' ').replace('\n', ' ')
                    article.source = link
                    article.save()
                else:
                    logging.error('Заданный узел не доступен ', r.status_code)

        except requests.exceptions.RequestException as connerr:
            logging.error(connerr)
