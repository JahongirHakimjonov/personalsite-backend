from rest_framework import serializers

from apps.portfolio.models import ContactInfo


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"
