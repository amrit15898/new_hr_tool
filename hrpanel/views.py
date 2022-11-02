from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.
class IntervieApi(APIView):
    def get(self, request):
        objs = Interview.objects.filter(is_delete=False)
        serializer = InterviewSerializer(objs, many=True)

        return Response({
            "status": True, 
            "data": serializer.data
        })

    def post(self, request):
        data = request.data
        print(data)
       
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

    def patch(self, request):
        data = request.data 
        obj = Interview.objects.get(id=data.get('id'))
        serializer = InterviewSerializer(obj, data = data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "data sucessfully updated",
                "data": serializer.data

            })

        return Response({
            "status": False, 
            "message": serializer.errors 
        })

    def put(self, request):
        data = request.data 
        
        obj = Interview.objects.get(id=data.get('id'))
        
        serializer = InterviewSerializer(obj, data = data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "data sucessfully updated",
                "data": serializer.data

            })

        return Response({
            "status": 200,
            "message": "something went wrong",
            "message": serializer.errors
        })

    def delete(self, request):
        data = request.data
        obj = Interview.objects.get(id=data.get('id'))
        obj.is_delete = True
        obj.save()

        return Response({
            "status": True , 
            "message": "data sucessfully deleted"

        })

    


        

class MeetingApi(APIView):
    def get(self, request):
        objs = Meeting.objects.all()
        serializer = MeetingSerializer(objs, many=True)

        return Response({
            "status": True, 
            "data": serializer.data
        })

    def post(self, request):
        data = request.data
        
        serializer = MeetingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True, 
                "data": serializer.data

            })

        return Response({
            "status": 200,
            "message": serializer.errors
        })

    
    def patch(self, request):
        data = request.data 
        obj = Meeting.objects.get(id=data.get('id'))
        serializer = MeetingSerializer(obj, data = data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "data sucessfully updated",
                "data": serializer.data

            })

    def put(self, request):
        data = request.data 
        obj = Meeting.objects.get(id=data.get('id'))
        serializer = MeetingSerializer(obj, data = data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "data sucessfully updated",
                "data": serializer.data

            })

    def delete(self, request): 
        data = request.data
        obj = Meeting.objects.get(id=data.get('id'))
        obj.delete()

        return Response({
            "stauts": 200,
            "message": "Deleted", 
        

        })

        