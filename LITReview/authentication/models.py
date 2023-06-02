from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_photo = models.IntegerField(null=True)
