from rest_framework import serializers

from apps.portfolio.models import Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"
