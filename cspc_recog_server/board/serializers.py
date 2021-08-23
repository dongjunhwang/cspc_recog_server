from rest_framework import serializers
from .models import Board, Post, Comment, PostImage

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('board_id','id','title','author','contents','created_date','like_count','like_members','has_image')

class PostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = PostImage
        fields = ['image']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('board_id','id','title','author','contents','created_date','like_count','has_image')

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post_id','author','contents','created_date')

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','like_count')

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('board_name','group_id')

    def create(self, validated_data):
        board = Board.objects.create(**validated_data)
        return board