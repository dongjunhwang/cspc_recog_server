from django.db import models

# Create your models here.
class Club(models.Model):
    club_name = models.CharField(max_length=30)

class Board(models.Model):
    board_name = models.CharField(max_length=30)
    club_id = models.ForeignKey(Club,on_delete=models.CASCADE)

class Post(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='board',default='')
    title = models.CharField(max_length=50,null = False)
    author = models.CharField(max_length=10,null = False)
    contents = models.TextField(null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    like_count = models.IntegerField(default=0)

class comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=10, null=False)
    contents = models.TextField(null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)