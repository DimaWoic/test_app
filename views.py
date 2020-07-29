from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from rest_framework.pagination import PageNumberPagination


class ArticlePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30
    last_page_strings = ('the_end',)


class ArticleView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    pagination_class = ArticlePagination


class DetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
