from rest_framework import viewsets
from badnews.models import Author, News
from badnews.serializers import AuthorSerializer, NewsSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class NewsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer

