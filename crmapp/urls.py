from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cards', views.cards, name='cards'),
    path('dash', views.dash, name='dash'),
    
    path('archives', views.archives, name='archives')
]