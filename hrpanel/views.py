from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class IntervieApi(APIView):
    def get(self, request):
        objs = Interview.objects.all()
        serializer = InterviewSerializer(objs, many=True)

        return Response({
            "status": True, 
            "data": serializer.data
        })

    def post(self, request):
        data = request.data
        dt = str(data.get('datetime'))
      
        list1 = dt.split("T")
        for obj in Interview.objects.all():
            if(str(obj.datetime.date()) == list1[0]):
                if(int(obj.datetime.hour) == int(list1[1][0:2])):
                    return Response({
                        "status": False, 
                        "messge":"time alread booked"
                    })  
        serializer = InterviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 200,
                "message": "data fetched",
                "data": request.data
            })

        return Response({
            "status": False, 
            "message": "somethign went wrong",
            "errors": serializer.errors
        })

        

class MeetingApi(APIView):
    def get(self, request):
        objs = Meeting.objects.all()
        serializer = MeetingSerializer(objs, many=True)

        return Response({
            "status": True, 
            "data": serializer.data
        })