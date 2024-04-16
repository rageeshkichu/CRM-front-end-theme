from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('navbar', views.navbar, name='navbar'),
    path('cards', views.cards, name='cards'),
    path('dash', views.dash, name='dash'),
    path('navbar2',views.navbar2, name='navbar2'),
    path('archives', views.archives, name='archives')
]