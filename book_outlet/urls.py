from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.bookDetail, name="book-detail")
]