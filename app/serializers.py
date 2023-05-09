from rest_framework import serializers
from .models import *


class HackathonSerializer(serializers.ModelSerializer):
    class Meta():
        model = Hackathon
        fields = '__all__'

