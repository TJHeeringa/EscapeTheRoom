from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    pass


admin.site.register(Room, RoomAdmin)
admin.site.register(User, UserAdmin)
