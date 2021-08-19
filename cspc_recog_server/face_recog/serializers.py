from rest_framework import serializers
from .models import Face
from users.serializers import ProfileSerializer

class FaceSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Face
        fields = '__all__'

        # Profile의 모든 field를 serializer함.