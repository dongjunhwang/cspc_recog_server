from users.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FaceSerializer
from .models import Face
from .deepface import DeepFaceRecog

from django.contrib.auth.models import User
from django.http import JsonResponse

class FaceRecog(APIView):
    def post(self, request):
        # TODO : Group 별로 분리
        jsonData = request.data[0]
        image = jsonData['image']
        try:
            faces = Face.objects.all()
            profile = DeepFaceRecog(faces, image)
            if profile.is_online:
                profile.is_online = False
            else:
                profile.is_online = True
            profile.save()
            data = {
                "username": profile.user_id.username,
                "isOnline": int(profile.is_online),
                "response": 1
            }
            return JsonResponse(data, status=200)
        except:
            data = {
                "response": 0
            }
            return Response(data, status=404)


class FaceAdd(APIView):
    def post(self,request):
        #print(type(request.data[0]))
        jsonData = request.data[0]
        name =jsonData['username']
        image = jsonData['image']
        try:
            user = User.objects.get(username=name) #request.user
            profile = user.profile.all()[0]
            #group을 아직 넘기지 않으므로 일단 첫번째 것만 가져오게 된다.

            face =Face.objects.create(profile = profile, image_base64=image)
            face_serializer = FaceSerializer(face)
            return Response(face_serializer.data, status=200)
        except Profile.DoesNotExist:
            return Response(status=404)


    def get(self,request):
        face_serializer = FaceSerializer(Face.objects.all(), many = True)
        return Response(face_serializer.data, status = 200)