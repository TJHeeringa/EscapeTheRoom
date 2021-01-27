from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Room


def index(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, "index.html", context)


# @xframe_options_exempt
def room(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {
        "room": room
    }
    return render(request, "room.html", context)
