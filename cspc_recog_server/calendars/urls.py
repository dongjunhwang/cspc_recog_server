from django.urls import path, include
from .views import *

urlpatterns = [
    path("all/", calendarAPI),
    path("event/<int:pk>/", eventAPI),
    path("event/post/<int:pk>/",eventPostAPI)
]