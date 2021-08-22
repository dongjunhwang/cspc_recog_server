from rest_framework import serializers
from .models import Board, Post, Comment

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('board_id','id','title','author','contents','created_date','like_count','like_members')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('board_id','id','title','author','contents','created_date','like_count','like_members')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author','contents','created_date')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','like_count')