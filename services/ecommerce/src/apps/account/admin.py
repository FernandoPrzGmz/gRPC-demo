from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as _UserAdmin

User = get_user_model()

class UserAdmin(_UserAdmin):
    pass

admin.site.register(User, UserAdmin)
