from rest_framework.serializers import ModelSerializer
from .models import *
from .cipher import *

class LogUpSerializer(ModelSerializer):
        class Meta:
                model = Users
                fields = ["id", "username", "email", "password"]
                extra_kwargs = {"password": {"write_only": True}}
        
        # def create(self, validated_data):
        #         password = validated_data.pop('password', None)
        #         instance = self.Meta.model(**validated_data)
        #         if password is not None:
        #                 instance.set_password(password)
        #         instance.save()
        #         return instance
        


class LogInSerializer(ModelSerializer):
        class Meta:
                model = Users
                fields = ["id", "username", "password"]
                extra_kwargs = {"password": {"write_only": True}}
        
        # def login(self, validated_data):
        #         password = validated_data.pop('password', None)
        #         instance = self.Meta.model(**validated_data)
        #         if password is not None:
        #                 instance.set_password(password)
        #         instance.save()
        #         return instance


class LoggSerializer(ModelSerializer):
        class Meta:
            model = Logg
            fields = ["id", "log", "created_at"]
        #     extra_kwargs = {"log": {"write_only": True}}



