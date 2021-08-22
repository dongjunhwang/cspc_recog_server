from django.db import models
from users.models import Group, Profile
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
    board_name = models.CharField(max_length=30)
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE)

class Post(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='board',default='')
    title = models.CharField(max_length=50,null = False)
    author = models.CharField(max_length=10,null = False)
    contents = models.TextField(null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    like_count = models.IntegerField(default=0)
    like_members = models.ManyToManyField(Profile,related_name='like_post',blank=True)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=10, null=False)
    contents = models.TextField(null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)