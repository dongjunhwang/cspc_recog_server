from datetime import datetime, timedelta
from pytz import timezone

from users.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FaceSerializer
from .models import Face
from .deepface import DeepFaceRecog, DeepFaceAdd

from django.contrib.auth.models import User
from django.http import JsonResponse

class FaceRecog(APIView):
    def post(self, request):
        # TODO : Group 별로 분리
        image = request.POST.get('image')


        faces = Face.objects.all()
        profile = DeepFaceRecog(faces, image)
        if profile:
            current_visit_time = datetime.now(timezone('Asia/Seoul')) - profile.last_visit_time
            if current_visit_time > timedelta(seconds=20):#20초 안에 또 나가면 퇴실처리 안됨.
                if profile.is_online:
                    # 누적 visit time 저장
                    profile.visit_time_sum += current_visit_time
                    profile.is_online = False
                else:
                    profile.last_visit_time = datetime.now()
                    profile.is_online = True
                profile.save()
                data = {
                    "username": profile.user_id.username,
                    "isOnline": int(profile.is_online),
                    "response": 1 #입실 혹은 퇴실에 성공했습니다.
                }
                return JsonResponse(data, status=200)
            else:
                data = {"response": 2} # 좀 있다가 퇴실하세요
                return JsonResponse(data, status=200)
        else:
            data = {"response": 0} # 얼굴을 추가하세요 얼굴이 없네요
            return JsonResponse(data, status=200)
        return Response(status=404)


class FaceAdd(APIView):
    def post(self,request):
        #print(type(request.data[0]))
        jsonData = request.POST
        name =jsonData.get('username')
        image = jsonData.get('image')
        try:
            user = User.objects.get(username=name) #request.user
            profile = user.profile.all()[0]
            #group을 아직 넘기지 않으므로 일단 첫번째 것만 가져오게 된다.
            face =Face.objects.create(profile = profile, image=DeepFaceAdd(image))
            face_serializer = FaceSerializer(face)
            return Response(face_serializer.data, status=200)
        except Profile.DoesNotExist:
            return Response(status=404)


    def get(self,request):
        face_serializer = FaceSerializer(Face.objects.all(), many = True)
        return Response(face_serializer.data, status = 200)