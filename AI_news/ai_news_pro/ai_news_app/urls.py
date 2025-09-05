from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("api/news/", views.get_news, name="get_news"),
]
