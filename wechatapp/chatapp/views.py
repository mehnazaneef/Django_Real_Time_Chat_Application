from django.shortcuts import render
from .models import Room, Message

def rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'rooms.html', context)

def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    context = {'room':room, 'messages':messages}
    return render(request, 'room.html', context)
