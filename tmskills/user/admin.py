from django.contrib import admin
from user.models import User


class AdminUser(admin.ModelAdmin):
    list_display = ["username", "email"]


admin.site.register(User, AdminUser)