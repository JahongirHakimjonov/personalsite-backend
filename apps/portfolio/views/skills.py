from rest_framework.response import Response
from rest_framework.views import APIView

from apps.portfolio.models.skills import Skill
from apps.portfolio.serializers.skills import SkillSerializer


class SkillView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
