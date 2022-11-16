
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# class AccessHrAndAdmin(BasePermission):
#     def has_permission(self, request, view):
#         now_user = request.user
#         # print(now_user.domain)
#         try:
#             user = User.objects.get(username=now_user)
#         except Exception as e:
#             print(e)
            
        
      
#         if user.domain.name == "HR" or user.is_staff or user.domain.name=="MD":
            

#             return True

        
            


# class UserApi(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

    

#     def get(self, request):
        
#         users = User.objects.filter(is_delete=False)
#         serializer = UserSerializer(users, many=True)

#         return Response({
#             "status": 200,
#             "message": "Get method called",
#             "data": serializer.data
#         })

#     def post(self, request):
#         data = request.data 
#         user = request.user

#         context = {
#             "user": user
#         }


        
#         serializer = UserSerializer(data = data, context = context)

#         if serializer.is_valid():
#             serializer.save()
#             user = User.objects.get(username=serializer.data["username"])
#             refresh = RefreshToken.for_user(user)

#             return Response({
#                 "status": 200, 
#                 "data": "data saved",
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token)

#             })

#         return Response({
#             "message": "something went wrong",
#             "error": serializer.errors

#         })

#     def delete(self, request):
#         data = request.data
#         obj = User.objects.get(id=data.get('id'))
#         obj.is_delete = True
#         obj.save()
#         return Response({
#             "message": "data succssfully deleted"
#         })

#     def patch(self, request):
#         data = request.data 
#         try:

#             obj = User.objects.get(id=data.get('id'))

#         except User.DoesNotExist:
#             return Response(
#                 {
#                     "message": "id required"
#                 }
#             )
#         data = request.data 
#         user = request.user

#         context = {
#             "user": user
#         }


        
        
#         serializer = UserSerializer(obj, data=data, partial=True, context = context)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "status": True, 
#                 "message": "data successfully updated",
#                 "data": serializer.data

#             })

#         return Response({
#             "status": False, 
#             "message": "something went wrong",
#             "errors": serializer.errors

#         })
from rest_framework.viewsets import ViewSet
class UserApi(ViewSet):
   
    def list(self, request, *args, **kwargs):
      
        # params = kwargs
        # print(params)

        # print(params)
        objs = User.objects.filter(is_delete=False)

        serializer = UserSerializer(objs, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        obj = User.objects.get(id=pk)
        serializer = UserSerializer(obj)
        return Response(serializer.data)
    
    def create(self, request):
        data =request.data 
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "data succesfully added"

            })
            
        return Response({
            "message": "something went wrong",
            "error": serializer.errors
        })
        
    def destroy(self, request, pk):
        try:
            
            obj = User.objects.get(id=pk)
            obj.is_delete =True
            obj.save()
        except User.DoesNotExist:
            return Response({
                "message": "id not ex"
                
            })

        return Response({
            "message": "user deleted"

        })
        
    def partial_update(self, request, pk):

        obj = User.objects.get(id=pk)
        serializer = UserSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user updated succesfully"})
        
        return Response({
            "message": "id required"

        })
        
    def update(self, request, pk):
        return Response({
            "message": "update called"
        })

        

    
    
        
       
