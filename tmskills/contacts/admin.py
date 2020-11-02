from django.contrib import admin
from contacts.models import FeedBack


class AdminFeedBack(admin.ModelAdmin):
    list_display = ["fullname", "is_worked"]


admin.site.register(FeedBack, AdminFeedBack)
