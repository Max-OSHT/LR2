from django.contrib import admin
from django.urls import path, include
from back.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register('', ViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
