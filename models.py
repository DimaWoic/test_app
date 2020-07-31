from django.db import models


class Article(models.Model):
    """модель таблицы базы данных Article, содержащая следующие поля:
            title - заголовок статьи, с параметром unique = True, препядствует
                    добавлению повторяющихся заголовков
            text -  текст статьи
            source - ссылка на оригинал статьи
            published - дата и время для сортировки

    """

    title = models.CharField(max_length=250, unique=True, verbose_name='заголовок статьи')
    text = models.TextField(verbose_name='текст статьи')
    source = models.URLField(verbose_name='ссылка на оригинал')
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Метамодель Meta служит для корректного отображения данных модели
        в интерфейсе администратора и не является обязательной, не является полем
        """

        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['published']

    def __str__(self):
        """Метод def __str__(self): предназначен для корректного отображения
        записи в списке записей в интерфейсе администратора
        """

        return self.title
