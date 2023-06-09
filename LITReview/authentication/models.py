from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    profile_photo = models.ImageField(
        null=True, blank=True, verbose_name='photo de profile')
    follows = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        symmetrical=False,
        through='UserFollows',
        related_name='followers')


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following')
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by')
    user_name = models.CharField(
        max_length=128, blank=True)
    followed_user_name = models.CharField(
        max_length=128, blank=True)


    class Meta:
        unique_together = ('user', 'followed_user', )
