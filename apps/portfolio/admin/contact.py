from django.contrib import admin

from apps.portfolio.models import ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "address")
    search_fields = ("email", "phone", "address")
