from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import HackathonSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView
from .models import *
# Create your views here.

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

        

