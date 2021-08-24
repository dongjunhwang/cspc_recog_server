# board/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path("group/<int:pk>",views.BoardAPI.as_view()),
    path("<int:pk>", views.PostList.as_view()),
    path('post/<int:pk>', views.PostAPI.as_view()),
    path('comment/<int:pk>', views.CommentAPI.as_view()),
    path('like/<int:pk>',views.PostLike.as_view()),
    path('image/<int:pk>',views.PostImageAPI.as_view()),
    path('newboard',views.BoardAPI.as_view()),
]