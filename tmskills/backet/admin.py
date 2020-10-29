from django.contrib import admin
from backet.models import Bucket


class AdminBucket(admin.ModelAdmin):
    list_display = ["user", "item"]


admin.site.register(Bucket, AdminBucket)