import re
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from tutor.models import Roadmap, Section, SubSection, AuthUser
from tutor.serializer import RoadmapSerializer, SectionSerializer, SubSectionSerializer, AuthUserSerializer, AuthTokenSerializer #, AuthCustomTokenSerializer #RegistrationSerializer, LoginSerializer, ListSerializer, #, AuthLoginUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status



class Signup(CreateAPIView):
    serializer_class = AuthUserSerializer
    queryset = AuthUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({
            'token': token.key,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role
            }, status=status.HTTP_201_CREATED, headers=headers)


#views to make login for user using email and password, generating token for user
class AuthLoginUser(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role
            })

class SectionGen(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

class SectionGenDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

class RoadmapGen(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = RoadmapSerializer
    queryset = Roadmap.objects.all()
    

class RoadmapGenDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = RoadmapSerializer
    queryset = Roadmap.objects.all()
    
class SubSectionGen(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = SubSectionSerializer
    queryset = SubSection.objects.all()

class SubSectionGenDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = SubSectionSerializer
    queryset = SubSection.objects.all()






    
    







