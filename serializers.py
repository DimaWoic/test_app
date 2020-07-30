from rest_framework import serializers


class ArticleListSerializer(serializers.Serializer):
    """class ArticleListSerializer - наследуется от rest_framework.serializers.Serializer
            предназначен для создания API листинга всех статей. Содержит следующие поля:
            id - идентификатор статьи
            title - поле заголовка статьи
            text - поле текста статьи, чтобы отобразить первые 700 символов, применено поле
                 SerializerMethodField с методом:
                     def get_text(self, obj):
                         return obj.text[:700]
    """

    id = serializers.IntegerField()
    title = serializers.CharField()
    text = serializers.SerializerMethodField()

    def get_text(self, obj):
        return obj.text[:700]


class ArticleSerializer(serializers.Serializer):
    """class ArticleSerializer - наследуется от rest_framework.serializers.Serializer
                предназначен для создания API отдельной статьи. Содержит следующие поля:
                title - поле заголовка статьи
                text - поле текста статьи, чтобы отобразить первые 700 символов, применено поле
                source - поле типа URLField, предназначено для вывода url-источника статьи
        """

    title = serializers.CharField()
    text = serializers.CharField()
    source = serializers.URLField()