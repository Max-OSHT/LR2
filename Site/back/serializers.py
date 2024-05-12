from django.contrib.auth import get_user_model, password_validation
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token 
from .models import *
from .cipher import *
from django_db_logger.models import StatusLog

class LogUpSerializer(ModelSerializer):
        class Meta:
                model = Users
                fields = ["id", "username", "email", "password"]
                extra_kwargs = {"password": {"write_only": True}}
        

class LogInSerializer(ModelSerializer):
        class Meta:
                model = Users
                fields = ["id", "username", "password"]
                extra_kwargs = {"password": {"write_only": True}}
        

class LoggSerializer(ModelSerializer):
        class Meta:
            model = StatusLog
            fields = ["id", "data"]
        #     extra_kwargs = {"log": {"write_only": True}}

class EmptySerializer(ModelSerializer):
        pass


