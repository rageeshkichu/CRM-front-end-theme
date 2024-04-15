from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('navbar', views.navbar, name='navbar'),
    path('home2', views.home2, name='home2'),
    path('dash', views.dash, name='dash')
]