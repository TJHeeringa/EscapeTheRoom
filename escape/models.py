from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    google_forms_link = models.CharField(max_length=250)
    photo = models.FileField(upload_to="escape/rooms/")

    def __str__(self):
        return self.name
