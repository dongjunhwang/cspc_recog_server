# Create your views here.

# board/views.py

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Post, Comment, PostImage
from .serializers import PostSerializer, CommentSerializer, PostListSerializer, LikeSerializer, PostImageSerializer
import json
# Create your views here.

class PostList(APIView):

    #게시물 목록 받아오기
    def get(self, request,pk):
        all_post = Post.objects.filter(board_id = pk)
        serializer = PostSerializer(all_post, many=True)
        return Response(serializer.data)

    #게시물 생성
    #board_id, id, title, author, contents 필요
    def post(self, request, pk):
        serializer = PostSerializer(data=request.data)
        image_flag = False
        if serializer.is_valid():
            post = serializer.save()
            # 이미지 업로드
            images_data = request.FILES
            for image in images_data.getlist('image'):
                if not image_flag:
                    post.has_image = True
                    post.save()
                    image_flag = True
                PostImage.objects.create(post_id=post.id, image=image)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostImageAPI(APIView):
    def get(self, request, pk):
        post_iamge = PostImage.objects.filter(post_id = pk)
        serializer = PostImageSerializer(post_iamge, many=True)
        return Response(serializer.data)

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
            post.like_count -= 1
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

class CommentAPI(APIView):
    #pk 게시글의 댓글 목록 가져오기
    def get(self,request,pk):
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

        # comments = comment.objects.filter(post_id = pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    #게시글에 댓글 올리기
    #post_id, author, contents 필요
    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)