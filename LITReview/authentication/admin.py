from django.contrib import admin
from .models import User, UserFollows

admin.site.register(User)
admin.site.register(UserFollows)
