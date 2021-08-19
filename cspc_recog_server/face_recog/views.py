from users.models import Profile
from users.serializers import ProfileSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FaceSerializer
from .models import Face
from .deepface import DeepFaceRecog

class FaceRecog(APIView):
    def post(self, request):
        # TODO : Group 별로 분리
        jsonData = request.data[0]
        image = jsonData['image']
        #try:
        faces = Face.objects.all()
        profile = DeepFaceRecog(faces, image)
        print(profile)
        profile_serializer = ProfileSerializer(profile, isOnline=True)
        #TODO : 여기서 부터 잘 안됌.
        if profile_serializer.is_valid():
            profile_serializer.object.isOnline = True
            profile_serializer.save()

        return Response(profile_serializer.data, status=200)
        #except:
        #    return Response(status=404)


class FaceAdd(APIView):
    def post(self,request):
        #print(type(request.data[0]))
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