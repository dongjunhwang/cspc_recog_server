from django.urls import path
from .views import   RegistrationAPI, LoginAPI, UserAPI, UserView
app_name = 'users'
urlpatterns = [
    path('', UserView.as_view()),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('<int:profile_id>', UserView.as_view()),
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
]
