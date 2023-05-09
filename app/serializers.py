from rest_framework import serializers
from .models import *


class HackathonSerializer(serializers.ModelSerializer):
    class Meta():
        model = Hackathon
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta():
        model= Participant
        fields = '__all__'