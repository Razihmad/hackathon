from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import HackathonSerializer,ParticipantSerializer,SubmissionSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView,ListCreateAPIView,CreateAPIView,UpdateAPIView
from .models import *
import json
# Create your views here.

class UserRegisterView(APIView):
    def post(self,request,*args,**kwargs):
        user_serialzier = UserSerializer(data=request.data)
        if(user_serialzier.is_valid()):
            user_serialzier.save()
            return Response({"msg":"You have been registered successfully"},status=status.HTTP_201_CREATED)
        return Response(user_serialzier.errors,status=status.HTTP_400_BAD_REQUEST)


class HackathonAPIView(APIView):
    parser_classes = (MultiPartParser,FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]
    def post(self,request,*args,**kwargs):
        hackathon_serializer = HackathonSerializer(data=request.data)
        if(hackathon_serializer.is_valid()):
            hackathon_serializer.save()
            return Response({"msg":"hackathon created successfully"},status=status.HTTP_201_CREATED)
        return Response(hackathon_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class HackathonListView(ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class ParticipateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = ParticipantSerializer
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    


class HackathonSubmissionAPIView(ListCreateAPIView,UpdateAPIView):
    parser_classes = (MultiPartParser,FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]
    serializer_class = SubmissionSerializer
    def get_queryset(self):
        obj = Submission.objects.all().filter(user=self.request.user)
        return obj
    def perform_create(self,serializer):
        return serializer.save(user=self.request.user)

        