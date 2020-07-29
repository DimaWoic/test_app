from rest_framework import serializers


class ArticleListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    text = serializers.CharField()


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    text = serializers.CharField()
    source = serializers.URLField()