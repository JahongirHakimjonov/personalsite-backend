from django.contrib import admin

from apps.portfolio.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "date")
    search_fields = ("title", "description")
