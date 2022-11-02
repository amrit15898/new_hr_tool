from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain 

        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    def validate(self, data):
        user = self.context.get("user")
      
        obj = User.objects.get(username=user)
        print(data.get("domain").name)
        try:
            if (obj.domain.name=="HR") and data.get("domain").name =="MD":
                raise serializers.ValidationError("hr not create md")

        except Exception as e:
            raise serializers.ValidationError("role not find")


        email = User.objects.filter(email = data.get('email'))

        if email:
            raise serializers.ValidationError("email is already exits please try with diffrent email")
        

        phone = data.get('phone')
        phone_exits = User.objects.filter(phone=phone)

        if phone_exits:
            raise serializers.ValidationError("phone number already registerd try with another number")


        if (len(phone)>10 or len(phone)<10):
            raise serializers.ValidationError("please enter 10 digit number ")

        return data
