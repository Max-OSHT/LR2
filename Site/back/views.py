from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout 

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
   
# from .permissions import UserPermission
from back.models import *
from back.serializers import LogUpSerializer, LogInSerializer


class LogUpView(APIView):
    authentication_classes = [TokenAuthentication,]
    serializer_class = LogUpSerializer
    queryset = Users.objects.all()
    def post(self, request, *args, **kwargs):
        serializer = LogUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token, created = Token.objects.get_or_create(user=serializer.instance)
            ret = {'token': token.key, 'data': serializer.data}
            return Response(ret, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogInView(APIView):
    authentication_classes = [TokenAuthentication,]
    serializer_class = LogInSerializer
    queryset = Users.objects.all()
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = None

        if '@' in username:
            try:
                user = Users.objects.get(email=username)
            except ObjectDoesNotExist:
                pass
        
        if user:
            user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            if user:
                login(request, user)
                serializer = LogInSerializer(user)
                token, _ = Token.objects.get_or_create(user=user)
                ret = {'token': token.key, 'data': serializer.data}
                return Response(ret, status=200)
                # return Response(ret, status=status.HTTP_200_OK)
        else:
            ret = {'username': username, 'detail': 'Username or password is wrong'}
            return Response(ret, status=403)