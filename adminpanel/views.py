from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


# Create your views here.
class users_api(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response({
            "status": 200,
            "message": "Get method called",
            "data": serializer.data
        })

    def post(self, request):
        data = request.data 
        print(data)
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 200, 
                "data": "data saved"

            })

        return Response({
            "message": "something went wrong",
            "error": serializer.errors

        })

    def delete(self, request):
        data = request.data
        obj = User.objects.get(id=data.get('id'))
        obj.delete()
        return Response({
            "message": "data succssfully deleted"
        })

    def patch(self, request):
        data = request.data 
        obj = User.objects.get(id=data.get('id'))
        
        
        serializer = UserSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True, 
                "message": "data successfully updated",
                "data": serializer.data

            })

        return Response({
            "status": False, 
            "message": "something went wrong",
            "errors": serializer.errors

        })
       
