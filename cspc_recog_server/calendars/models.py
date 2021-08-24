from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=100)

class Calendar(models.Model):
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE)

class Event(models.Model):
    calendar_id = models.ForeignKey(Calendar,on_delete=models.CASCADE)

    title = models.CharField(max_length=50, null = False)
    description = models.TextField(null = False)
    date = models.DateTimeField(auto_now = False)
