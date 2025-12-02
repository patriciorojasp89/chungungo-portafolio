from django.contrib import admin
from .models import Step


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "is_completed", "created_at", "updated_at")
    list_filter = ("is_completed", "created_at")
    search_fields = ("title", "description")
    ordering = ("order",)
