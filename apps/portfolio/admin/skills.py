from django.contrib import admin

from apps.portfolio.models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
    search_fields = ("name", "image")
