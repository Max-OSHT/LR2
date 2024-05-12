# from django.contrib.auth.hashers import make_password, check_password 
# from django.core.exceptions import ObjectDoesNotExist
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# import logging
from rest_framework.permissions import IsAuthenticated, AllowAny

# from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response 
# from rest_framework.decorators import action
from rest_framework.views import APIView

# logger = logging.getLogger('django')

from django.contrib.auth import authenticate, logout, login
from django_db_logger.models import StatusLog
from .cipher import AESenc, AESdec, entry, out

import jwt, datetime
# from .permissions import UserPermission
from back.models import *
from back.serializers import LoggSerializer, EmptySerializer

class LogViewSet(APIView):
    data = " "
    permission_classes = [IsAuthenticated]
    serializer_class = LoggSerializer
    def get(self, request, *args, **kwargs):
        log = StatusLog.objects.all()
        log = LoggSerializer(log, many=True).data
        if request.user.is_superuser:
            for i in log:
                i['data'] = out(i['data'])     
            return Response({"log": log}, status=200)
        else:
            return Response({"log": log}, status=200)