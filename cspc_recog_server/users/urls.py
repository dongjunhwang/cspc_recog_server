from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.UserView.as_view()),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('<int:profile_id>', views.UserView.as_view()),
]
