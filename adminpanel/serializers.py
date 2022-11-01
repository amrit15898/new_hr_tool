from rest_framework import serializers
from .models import *
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