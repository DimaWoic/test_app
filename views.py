from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from rest_framework.pagination import PageNumberPagination


class ArticlePagination(PageNumberPagination):
    """class ArticlePagination - предназнчен для реализации пагинации в списка статей в API
                                 наследуется от rest_framework.pagination.PageNumberPagination, имеет следующие атрибуты
                                 page_size - количество выводимых данных поумолчанию на одной странице
                                 page_size_query_param - параметр для передачи в http-запросе о смене количества
                                                         выводимых записей на одной странице
                                 max_page_size - максимально возможное количество записей для одной страницы
                                 last_page_strings - выводимое сообщение при достижении последней страницы

    """

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30
    last_page_strings = ('end',)


class ArticleView(ListAPIView):
    """class ArticleView - выодит листинг статей и обрабатывает метод GET, наследуется от
                           rest_framework.generics.ListAPIView и имеет следующие атрибуты:
                           queryset - атрибут указывающий диспетчер записи, где будет осуществляться поиск записи
                           serializer_class - атрибут указывающий сериализатор
                           pagination_class - атрибут указывающий переопределённый класс пагинатора
    """

    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    pagination_class = ArticlePagination


class DetailView(RetrieveAPIView):
    """class DetailView - выодит отдельную статью и обрабатывает метод GET, наследуется от
                               rest_framework.generics.RetrieveAPIView и имеет следующие атрибуты:
                               queryset - атрибут указывающий диспетчер записи, где будет осуществляться поиск записи
                               serializer_class - атрибут указывающий сериализатор
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
