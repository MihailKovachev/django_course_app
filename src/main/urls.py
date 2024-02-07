from django.urls import path

from .views import index_view

urlpatterns = [
    path("", index_view, name = "main"),
    path("index", index_view, name = "main")
]
