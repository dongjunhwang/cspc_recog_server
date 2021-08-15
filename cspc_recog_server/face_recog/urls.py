from django.urls import path
from . import views

app_name = 'face'
urlpatterns = [
    path('detect', views.FaceRecog.as_view()),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('add', views.FaceAdd.as_view()),
]