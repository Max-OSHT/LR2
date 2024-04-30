from django.contrib.auth.hashers import make_password, check_password 
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response 
from rest_framework.decorators import action
from rest_framework import status, viewsets
from django.contrib.auth import authenticate

import jwt, datetime
   
# from .permissions import UserPermission
from back.models import *
from back.serializers import LogUpSerializer, LogInSerializer, EmptySerializer


class ViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny,]
    authentication_classes = [TokenAuthentication,]
    serializer_class = EmptySerializer
    queryset = Users.objects.all()

    @action(methods=['POST', ], detail=False)
    def logup(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = make_password(request.data.get('password'))
        data = {'username': username, 'email': email, 'password': password}
        serializer = LogUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        try:
            login = request.data['login']
            password = request.data['password']
            user = None
            if '@' in login:
                user = Users.objects.filter(email=login).first()
            else:
                user = Users.objects.filter(username=login).first()
            # user = authenticate(username=login, password=password)
            if user is None:
                raise AuthenticationFailed('User not found!')

            if not user.check_password(password):
                raise AuthenticationFailed('Incorrect password!')
            try:
                payload = {        
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                    'iat': datetime.datetime.utcnow()
                }
                token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
                response = Response(status=200)

                response.set_cookie(key='token', value=token, httponly=True)
                response.data = {
                    'user': user.username,
                    'token': token
                }
                return response
            except Exception as e:
                raise e
        except KeyError:
            res = {'error': 'please provide a email and a password'}
            return Response(res)
    
    @action(methods=['GET', ], detail=False)
    def user(self, request):
        token = request.COOKIES.get('token')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = Users.objects.filter(id=payload['id']).first()
        return Response({'user': user.username}, status=200)

    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        response = Response(status=200)
        response.delete_cookie('token')
        response.data = {
            'message': 'success'
        }
        return response