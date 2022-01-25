from django.urls import path
from .views import RegistrationAPI, LoginAPI, UserAPI, UserView, ProfileUpdateAPI, GroupUpdateAPI, ProfileCreateAPI, \
    GroupCreateAPI, ProfileAPI, GroupAPI
from knox import views as knox_views

app_name = 'users'
urlpatterns = [
    path('', UserView.as_view()),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('<int:profile_id>', UserView.as_view()),
    path('profile/update/<int:profile_id>',ProfileUpdateAPI.as_view()),

    # 회원가입, 로그인, 로그아웃
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/logout/", knox_views.LogoutView.as_view(), name='knox_logout'),


    path("auth/user/", UserAPI.as_view()),
    #path("auth/user/profile/", ProfileAPI.as_view()),
    path("auth/user/profile/<int:id>/", ProfileAPI.as_view()),
    path("auth/user/group/", GroupAPI.as_view()),

    path("auth/profile/<int:pk>/update/", ProfileUpdateAPI.as_view()),
    path("auth/group/<int:pk>/update/", GroupUpdateAPI.as_view()),

    path("auth/user/profile/", ProfileAPI.as_view()),
    path("auth/user/group/", GroupAPI.as_view()),

    path("auth/profile/create", ProfileCreateAPI.as_view()),
    path("auth/group/create", GroupCreateAPI.as_view()),

]
