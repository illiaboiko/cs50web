from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.show_article, name="show_article"),
    path("search/", views.search, name="search")
]
