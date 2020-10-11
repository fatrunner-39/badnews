from django.contrib import admin

from .models import Author
from .models import News

admin.site.register(Author)
admin.site.register(News)
