from django.contrib import admin

from apps.portfolio.models import Support


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ("full_name", "message", "email")
    search_fields = ("full_name", "message", "email")
