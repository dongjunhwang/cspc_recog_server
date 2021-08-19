from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
        # Profile의 모든 field를 serializer함.


"""
    def update(self, instance, validated_data):
        is_online = validated_data.pop('is_online')
        instance.is_online = is_online
        print(instance.is_online)
        instance.save()

        return instance
"""