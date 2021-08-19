# api/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path("board/<int:pk>", views.PostList.as_view()),
    path('comment/<int:pk>', views.commentAPI),
    path('like/<int:pk>',views.PostLike.as_view()),
]