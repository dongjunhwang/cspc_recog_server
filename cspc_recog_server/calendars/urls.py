from django.urls import path, include
from .views import *

urlpatterns = [
    path("all/", calendarAPI),
    path("<int:pk>/event/", EventAPIView.as_view()),
    path("<int:pk>/event/post/",EventAPIView.as_view()),
    path("<int:cal_id>/event/<int:event_id>/delete/",EventAPIView.as_view()),
    path("<int:cal_id>/event/<int:event_id>/edit/", EventAPIView.as_view()),
]