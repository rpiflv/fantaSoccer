from django.contrib import admin

from .models import Squad, AvailablePlayer, Profile, League


myModels = [Squad, AvailablePlayer, Profile, League]
admin.site.register(myModels)
