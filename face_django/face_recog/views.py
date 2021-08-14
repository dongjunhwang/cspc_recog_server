from users.models import Profile
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FaceSerializer
from .models import Face
class FaceRecog(APIView):
    def post(self,request):

        return Response("test ok", status=200)


class FaceAdd(APIView):
    def post(self,request):
        print(type(request.data[0]))
        jsonData = request.data[0]
        name =jsonData['username']
        image = jsonData['image']
        try:
            profile = Profile.objects.get(user__username = name)
            face =Face.objects.create(profile = profile, image_base64 = image)
            face_serializer = FaceSerializer(face)
            return Response(face_serializer.data, status=200)
        except Profile.DoesNotExist:
            return Response(status=404)


    def get(self,request):
        face_serializer = FaceSerializer(Face.objects.all(), many = True)
        return Response(face_serializer.data, status = 200)