from rest_framework import serializers


class ArticleListSerializer(serializers.Serializer):
    title = serializers.CharField()
    text = serializers.CharField(max_length=700)


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    text = serializers.CharField()
    source = serializers.URLField()