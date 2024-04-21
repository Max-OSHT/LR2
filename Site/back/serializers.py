from rest_framework.serializers import ModelSerializer
from .models import *
from .cipher import *

class UserSerializer(ModelSerializer):
        class Meta:
                model = Users
                fields = ["url", "username", "email", "password", "created_at"]
                extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
                user = Users(username=validated_data["username"])
                user.set_password(validated_data["password"])
                user.save()
                return user

class LoggSerializer(ModelSerializer):
        class Meta:
            model = Logg
            fields = ["id", "log", "created_at"]
            extra_kwargs = {"log": {"write_only": True}}
        
        def create(self, validated_data):
                log = Logg(id=validated_data["id"])
                log.entry(validated_data["log"])
                log.save()
                return log

