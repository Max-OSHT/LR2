from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns 
from rest_framework.authtoken import views
from back import views

urlpatterns = [ 
    path('logup/', views.LogUpView.as_view()), 
    path('login/', views.LogInView.as_view()),
] 