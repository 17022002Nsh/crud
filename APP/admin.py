from django.contrib import admin
from .models import TODO

@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "done_at", "is_done", "created_at")
