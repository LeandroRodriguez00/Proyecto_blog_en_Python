from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "sender", "receiver", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("subject", "body", "sender__username", "receiver__username")
