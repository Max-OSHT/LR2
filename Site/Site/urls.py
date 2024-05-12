from django.contrib import admin
from django.urls import path, include, re_path
from django import urls
from back.views import *

from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', LogViewSet.as_view()),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
