# board/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path("<int:pk>", views.PostList.as_view()),
    path('comment/<int:pk>', views.CommentAPI),
    path('like/<int:pk>',views.PostLike.as_view()),
]