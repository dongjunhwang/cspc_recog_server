# Create your views here.

# board/views.py

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostListSerializer, LikeSerializer
import json
# Create your views here.

class PostList(APIView):

    #게시물 목록 받아오기
    def get(self, request,pk):
        all_post = Post.objects.filter(board_id = pk)
        serializer = PostListSerializer(all_post, many=True)
        return Response(serializer.data)

    #게시물 생성
    #board_id, id, title, author, contents 필요
    def post(self, request, pk):
        serializer = PostListSerializer(data=request.data)
        #req = json.loads(request.body)
        print(request.POST['title'])
        print(request.POST['author'])
        print(request.POST['contents'])
        print(request.POST['board_id'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostLike(APIView):
    #좋아요 개수
    def get(self,request,pk):
        post = Post.objects.get(id = pk)
        serializer = LikeSerializer(post)
        return Response(serializer.data)

    #좋아요 누르기
    def post(self, request,pk):
        post = Post.objects.get(id=pk)
        profile = request.POST['profile']
        # 이미 좋아요를 누른 profile이면 좋아요 삭제
        if post.like_members.filter(id=profile).exists():
            #print("삭제")
            post.like_members.remove(profile)
        else:
            #print("추가")
            post.like_count += 1
            post.like_members.add(profile)
        post.save()
        return Response()

@api_view(['GET'])
def PostAPI(request):
    all_post = Post.objects.all()
    serializer = PostListSerializer(all_post, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def CommentAPI(request,pk):

    try:
        # pk(인스턴스의 id)값을 받아 어떤 인스턴스인지 특정
        # url slug로 pk값을 받도록 urls.py에서 설정해준다.
        comments = Comment.objects.filter(post_id=pk)
        # 받은 pk값으로 조회했을 때 해당하는 인스턴스가 없다면 출력할 에러 코드와 메시지를 설정한다.
    except Comment.DoesNotExist:
        return Response({'error': {
            'code': 404,
            'message': "Comment not found!"
        }}, status=status.HTTP_404_NOT_FOUND)

    #comments = comment.objects.filter(post_id = pk)
    serializer = CommentSerializer(comments, many = True)
    return Response(serializer.data)