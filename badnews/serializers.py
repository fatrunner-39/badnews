from rest_framework import serializers

from badnews.models import Author, News

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('authorsname', 'pubdate')

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('author', 'title', 'news_text')


