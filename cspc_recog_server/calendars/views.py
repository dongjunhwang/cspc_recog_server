from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Calendar, Event
from .serializers import CalendarSerializer, EventSerializer
import json

@api_view(['GET'])
def calendarAPI(request):
    all_calendar = Calendar.objects.all()
    serializer = CalendarSerializer(all_calendar, many=True)
    return Response(serializer.data)

class EventAPIView(APIView):
    def get(self, request, pk):
        all_event = Event.objects.filter(calendar_id = pk).order_by('date')
        serializer = EventSerializer(all_event, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        if request.method == 'POST':
            
            calendar_id = Calendar.objects.filter(id = pk)[0]
            
            request_data = json.loads(request.body.decode('utf-8'))[0]
            title = request_data['title']
            description = request_data['description']
            date = request_data['date']
            
            event = Event(calendar_id = calendar_id,
            title = title, description = description, date = date
            )
            event.save()
            
            return Response(True)

    def delete(self, request, cal_id, event_id):
        if request.method == 'DELETE':
            event = Event.objects.filter(id=event_id).delete()
            return Response("deleted")

    def put(self, request, cal_id, event_id):
        if request.method == 'PUT':
            
            event = Event.objects.get(id=event_id)
            
            request_data = json.loads(request.body.decode('utf-8'))[0]
            event.title = request_data['title']
            event.description = request_data['description']
            event.date = request_data['date']
            
            event.save()

            return Response(True)
