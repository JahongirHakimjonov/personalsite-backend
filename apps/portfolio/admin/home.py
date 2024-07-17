from django.contrib import admin

from apps.portfolio.models import Home


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")
    search_fields = ("title", "subtitle")
