from django.contrib import admin
from apps.users.models import CustomUser


@admin.register(CustomUser)
class MeinUser(admin.ModelAdmin):
    pass

