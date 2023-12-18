from django.contrib import admin

from .models import Group,Message,Room,Room_Message

# Register your models here.
admin.site.register(Group)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Room_Message)