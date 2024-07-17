from rest_framework import serializers

from apps.portfolio.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "name",
            "my_role",
            "url",
            "description",
            "tools",
            "date",
        ]

    def get_tools(self, obj):
        # Local import to avoid circular import
        from apps.portfolio.serializers import SkillSerializer
        tools = obj.tools.all()
        return SkillSerializer(tools, many=True).data
