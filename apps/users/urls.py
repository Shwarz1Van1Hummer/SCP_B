# from django.contrib import admin
from django.urls import path
from apps.users.views import *

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('anime/', animationview, name='anima'),
]
#<header style="margin-top:10px; width:100%; height:100%"><a href="{% url 'logout' %}" style="border:1px solid black; width:40px; height: 60px;">Выйти</a>