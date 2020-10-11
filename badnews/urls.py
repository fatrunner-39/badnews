from django.urls import path, include
from rest_framework.routers import DefaultRouter
from badnews import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename = 'Author')
router.register(r'newss', views.NewsViewSet, basename = 'News')

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
