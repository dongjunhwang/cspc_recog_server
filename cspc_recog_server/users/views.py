from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework import status
from .models import Profile


class UserView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('userId') is None:
            profileSerializer = ProfileSerializer(
                Profile.objects.all(), many=True)
            # user 전체 리스트 get
            return Response(profileSerializer.data, status=200)
        else:
            userId = kwargs.get('userId')
            profileSerializer = ProfileSerializer(
                get_object_or_404(Profile, user__id=userId))
            return Response(profileSerializer.data, status=200)
            # user 개인 정보 get

