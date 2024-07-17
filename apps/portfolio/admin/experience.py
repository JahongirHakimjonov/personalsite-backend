from django.contrib import admin

from apps.portfolio.models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "start_date", "end_date")
    search_fields = ("title", "company")
