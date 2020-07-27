from rest_framework import routers
from .views import ArticleView, DetailView
from django.urls import path


urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>/', DetailView.as_view()),
]
