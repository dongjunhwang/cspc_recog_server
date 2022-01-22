# Create your views here.

# board/views.py

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Post, Comment, PostImage, Board
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, PostImageSerializer, BoardSerializer
from django.core.paginator import Paginator
import json
# Create your views here.

class PostList(APIView):

    #게시물 목록 받아오기
    def get(self, request,pk):
        all_post = Post.objects.filter(board_id = pk).order_by('-created_date')
        page = request.GET.get('page','1')
        paginator = Paginator(all_post,'10')
        print(paginator.num_pages)
        page_obj = paginator.page(page)
        serializer = PostSerializer(page_obj, many=True)
        if(int(page) >= paginator.num_pages):
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

            return Response(data=post.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostAPI(APIView):
    # 게시물 하나 받아오기
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    # 게시글 삭제
    def delete(self, request, pk):
        if request.method == 'DELETE':
            try:
                Post.objects.filter(id=pk).delete()
                return Response("deleted")
            except:
                return Response("delete fail")

    #게시글 수정
    def put(self,request, pk):
        if(request.method == 'PUT'):
            post = Post.objects.get(id=pk)
            '''print('제목'+post.title)
            request_data = JSONParser().parse(request.body)
            print(request_data['title'])
            if 'title' in request_data:
                post.title = request_data['title']
            if 'contents' in request_data:
                post.contents = request_data['contents']
            post.save()'''
            serializer = PostSerializer(post, data = request.data)
            if serializer.is_valid():
                post = serializer.save()
                images_data = request.FILES
                PostImage.objects.filter(post=post).delete()
                for image in images_data.getlist('image'):

                    PostImage.objects.create(post_id=post.id, image=image)

                return Response(status = status.HTTP_200_OK)
            else :
                return Response(status = status.HTTP_400_BAD_REQUEST)
            #return Response("invalid request", status = status.HTTP_400_BAD_REQUEST)

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
    def post(self,request,pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def CommentDelete(request,pk):
    try:
        Comment.objects.filter(id=pk).delete()
        return Response("deleted")
    except:
        return Response("delete fail")


class BoardAPI(APIView):
    #group_id에 해당하는 board 목록 가져오기
    def get(self,request,pk):
        all_board = Board.objects.filter(group_id = pk)
        serializer = BoardSerializer(all_board, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #보드 생성
    #group_id, board_name 필요
    def post(self,request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
