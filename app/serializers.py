from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from datetime import datetime,timezone
from rest_framework.validators import UniqueValidator
# utc = pytz.UTC

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required=True,validators = [UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True,required=True)
    password2 = serializers.CharField(write_only=True,required=True)
    class Meta():
        model = User
        fields = ('username','email','password','password2')
    
    def validate(self, attrs):
        if(attrs['password']!=attrs['password2']):
            raise serializers.ValidationError("Password did not match")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class HackathonSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(default =  serializers.CurrentUserDefault(),queryset=User.objects.all())
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
        end_datetime = str(data['hackathon'].end_datetime)
        end_datetime = datetime.fromisoformat(end_datetime).astimezone(timezone.utc)
        curDatetime = datetime.now()
        curDatetime = str(curDatetime)
        curDatetime = datetime.fromisoformat(curDatetime).astimezone(timezone.utc)
        
        if(curDatetime>end_datetime):
            raise serializers.ValidationError("This Hackthon Registration Has Been Closed")
        if(Participant.objects.filter(user=self.context['request'].user,hackathon=data['hackathon']).exists()):
            raise serializers.ValidationError("You have already been registered")
        
        return data
    class Meta():
        model= Participant
        fields = '__all__'    
        
class SubmissionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),queryset=User.objects.all())
    def validate(self, attrs):
        end_datetime = str(attrs['hackathon'].end_datetime)
        end_datetime = datetime.fromisoformat(end_datetime).astimezone(timezone.utc)
        curDatetime = datetime.now()
        curDatetime = str(curDatetime)
        curDatetime = datetime.fromisoformat(curDatetime).astimezone(timezone.utc)
        if(curDatetime>end_datetime):
            raise serializers.ValidationError("This Hackthon Submission Has Been Closed")
        hackathon = attrs['hackathon']
        if(Participant.objects.filter(user=self.context['request'].user,hackathon=hackathon).exists()==False):
            raise serializers.ValidationError("You are not register for this hackathon!")
        return attrs
    
    class Meta():
        model= Submission
        fields = '__all__'

    