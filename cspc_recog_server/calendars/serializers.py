from rest_framework import serializers
from .models import Calendar, Event

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('id', 'group_id')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'calendar_id', 'title', 'description', 'start_date', 'end_date')