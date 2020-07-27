from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name='заголовок статьи')
    text = models.TextField(verbose_name='текст статьи')
    source = models.URLField(verbose_name='ссылка на оригинал')
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-published']

    def __str__(self):
        return self.title
