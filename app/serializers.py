from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class HackathonSerializer(serializers.ModelSerializer):
    class Meta():
        model = Hackathon
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default =  serializers.CurrentUserDefault(),queryset=User.objects.all())
    class Meta():
        model= Participant
        fields = '__all__'
        
        
class SubmissionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),queryset=User.objects.all())
    class Meta():
        model= Submission
        fields = '__all__'

    