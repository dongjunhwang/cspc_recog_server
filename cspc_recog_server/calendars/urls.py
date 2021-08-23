from django.urls import path, include
from .views import *

urlpatterns = [
    path("all/", calendarAPI),
    path("<int:pk>/event/", eventAPI),
    path("<int:pk>/event/post/",eventPostAPI),
    path("<int:cal_id>/event/<int:event_id>/delete/",eventDeleteAPI),
]