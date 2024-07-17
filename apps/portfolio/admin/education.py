from django.contrib import admin

from apps.portfolio.models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("school", "degree", "start_date", "end_date")
    search_fields = ("school", "degree")
