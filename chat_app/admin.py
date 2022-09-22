from django.contrib import admin
from .models import room_messages,rooms
# Register your models here.
admin.site.register(room_messages)
admin.site.register(rooms)