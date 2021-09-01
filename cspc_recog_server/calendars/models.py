from django.db import models
from users.models import Group

class Calendar(models.Model):
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE)

class Event(models.Model):
    calendar_id = models.ForeignKey(Calendar,on_delete=models.CASCADE)

    title = models.CharField(max_length=50, null = False)
    description = models.TextField(null = True, blank=True)
    start_date = models.DateTimeField(auto_now = False)
    end_date = models.DateTimeField(auto_now = False)
