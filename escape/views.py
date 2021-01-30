from django.conf import settings
from django.shortcuts import render


from .models import Room


def index(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
        "avatar_url": settings.MAIN_PAGE_AVATAR
    }
    return render(request, "index.html", context)


def room(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {
        "room": room
    }
    return render(request, "room.html", context)
