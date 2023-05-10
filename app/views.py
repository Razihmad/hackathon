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


class HackathonAPIView(ListCreateAPIView):
    parser_classes = (MultiPartParser,FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]
    serializer_class = HackathonSerializer
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    def get_queryset(self):
        obj = Hackathon.objects.all()
        return obj
        
class EnrolledHackathonsListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    def get(self,request,*args,**kwargs):
        out = []
        temp = Participant.objects.filter(user=request.user)
        for i in temp:
            out.append(i.hackathon)
        hacakthon_serilzer = HackathonSerializer(out,many=True)
        return Response(hacakthon_serilzer.data)
    
class OwnersHackathonList(APIView):
    def get(self,request,*args,**kwargs):
        if(request.user.is_anonymous):
            return Response({"msg":"Unauthorized"},status=status.HTTP_401_UNAUTHORIZED)
        else:
            obj = Hackathon.objects.all().filter(owner=request.user)
            serializer = HackathonSerializer(obj,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

    
    
class ParticipateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = ParticipantSerializer
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    


class HackathonSubmissionAPIView(ListCreateAPIView,UpdateAPIView):
    parser_classes = (MultiPartParser,FormParser)
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = SubmissionSerializer
    def perform_create(self,serializer):
        return serializer.save(user=self.request.user)


class SubmissionsList(ListAPIView):
    parser_classes = (MultiPartParser,FormParser)
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = SubmissionSerializer
    def get_queryset(self):
        obj = Submission.objects.all().filter(user=self.request.user)
        return obj