from django.contrib import admin
from item.models import Item


class AdminItem(admin.ModelAdmin):
    list_display = ("brend", "model")

admin.site.register(Item, AdminItem)