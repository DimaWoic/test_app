from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class ArticlePagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 200
    last_page_strings = ('the_end',)


class ArticleView(ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination