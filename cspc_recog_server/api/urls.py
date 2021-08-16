# api/urls.py

from django.urls import path, include
from .views import HelloAPI, postAPI
from . import views
urlpatterns = [
    path("hello/", HelloAPI),
    path("post/wo/", postAPI),
    path('post/<int:pk>', views.commentAPI),
]