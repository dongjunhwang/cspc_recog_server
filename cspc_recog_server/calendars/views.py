from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Calendar, Event
from .serializers import CalendarSerializer, EventSerializer

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def calendarAPI(request):
    all_calendar = Calendar.objects.all()
    serializer = CalendarSerializer(all_calendar, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def eventAPI(request, pk):
    all_event = Event.objects.filter(calendar_id = pk)
    serializer = EventSerializer(all_event, many=True)
    return Response(serializer.data)
