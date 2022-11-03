
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated , IsAdminUser, BasePermission

class AccessHrAndAdmin(BasePermission):
    def has_permission(self, request, view):
        now_user = request.user
        # print(now_user.domain)
        try:
            user = User.objects.get(username=now_user)
        except Exception as e:
            print(e)
            
        
        try:
            if user.domain.name == "HR" or user.is_staff or user.domain.name=="MD":
            

                return True

        except Exception as e:
            print(e)

            


class users_api(APIView):
    permission_classes = [AccessHrAndAdmin]

    

    def get(self, request):
        
        users = User.objects.filter(is_delete=False)
        serializer = UserSerializer(users, many=True)

        return Response({
            "status": 200,
            "message": "Get method called",
            "data": serializer.data
        })

    def post(self, request):
        data = request.data 
        user = request.user

        context = {
            "user": user
        }


        
        serializer = UserSerializer(data = data, context = context)
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
        obj.is_delete = True
        obj.save()
        return Response({
            "message": "data succssfully deleted"
        })

    def patch(self, request):
        data = request.data 
        obj = User.objects.get(id=data.get('id'))
        data = request.data 
        user = request.user

        context = {
            "user": user
        }
        
        
        serializer = UserSerializer(obj, data=data, partial=True, context = context)
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
       
