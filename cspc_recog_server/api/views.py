# Create your views here.

# api/views.py

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Post, comment
from .serializers import PostSerializer, CommentSerializer, PostListSerializer

# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def postAPI(request):
    print("여기!")
    allPost = Post.objects.all()
    serializer = PostListSerializer(allPost, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def commentAPI(request,pk):
    print("여기!111")
    #allPost = Post.objects.all()
    #serializer = PostListSerializer(allPost, many=True)

    try:
        # pk(인스턴스의 id)값을 받아 어떤 인스턴스인지 특정
        # url slug로 pk값을 받도록 urls.py에서 설정해준다.
        comments = comment.objects.filter(post_id=pk)
        # 받은 pk값으로 조회했을 때 해당하는 인스턴스가 없다면 출력할 에러 코드와 메시지를 설정한다.
    except comment.DoesNotExist:
        return Response({'error': {
            'code': 404,
            'message': "Comment not found!"
        }}, status=status.HTTP_404_NOT_FOUND)

    #comments = comment.objects.filter(post_id = pk)
    serializer = CommentSerializer(comments, many = True)
    return Response(serializer.data)