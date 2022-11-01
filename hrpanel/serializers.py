from rest_framework import serializers
from .models import *
class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview

        fields = "__all__"


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting

        fields = "__all__"