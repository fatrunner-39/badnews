from django.db import models


class Author(models.Model):
    authorsname = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')


class News(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    news_text = models.TextField()
