from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms ,name='home'),
    path('room/<str:slug>/', views.room, name="room"),
]