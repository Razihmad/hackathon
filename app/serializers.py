from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from datetime import datetime,timezone
# utc = pytz.UTC

class HackathonSerializer(serializers.ModelSerializer):
    def validate(self,data):
        if(data['start_datetime']>=data['end_datetime']):
            raise serializers.ValidationError("End Date Time Must Be After Start Date Time")
        return data
    class Meta():
        model = Hackathon
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default =  serializers.CurrentUserDefault(),queryset=User.objects.all())
    def validate(self, data):
        hackathon = Hackathon.objects.get(title=data['hackathon'])
        end_datetime = str(hackathon.end_datetime)
        end_datetime = datetime.fromisoformat(end_datetime).astimezone(timezone.utc)
        curDatetime = datetime.now()
        curDatetime = str(curDatetime)
        curDatetime = datetime.fromisoformat(curDatetime).astimezone(timezone.utc)
        
        if(curDatetime>end_datetime):
            raise serializers.ValidationError("This Hackthon Registration Has Been Closed")
        return data
    class Meta():
        model= Participant
        fields = '__all__'    
        
class SubmissionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),queryset=User.objects.all())
    class Meta():
        model= Submission
        fields = '__all__'

    