from rest_framework import serializers
from .models import *
from adminpanel.serializers import UserSerializer

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        # interviewrs = UserSerializer(many = True, read_only = True)
        model = Interview

        fields = "__all__"

    def validate(self, data):

        dt = str(data.get('datetime'))
       
        list1 = dt.split(" ")

        for obj in Interview.objects.all():
            if(str(obj.datetime.date()) == list1[0]):

                if(int(obj.datetime.hour) == int(list1[1][0:2])):
                    raise serializers.ValidationError({"error": "this time is already booked set different time"})
        

        return data                                            


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting

        fields = "__all__"

    def validate(self, data):
        dt = str(data.get('date_time'))
      
        list1 = dt.split("T")
        for obj in Meeting.objects.all():
            if(str(obj.date_time.date()) == list1[0]):
                if(int(obj.date_time.hour) == int(list1[1][0:2])):
                    raise serializers.ValidationError({"error": "this time is alread booked"})



        return data