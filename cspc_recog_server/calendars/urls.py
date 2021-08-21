from django.urls import path, include
from .views import *

urlpatterns = [
    path("hello/", helloAPI),
    path("all/", calendarAPI),
    path("event/<int:pk>/", eventAPI),
]