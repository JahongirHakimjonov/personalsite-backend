from rest_framework.response import Response
from rest_framework.views import APIView

from apps.portfolio.models.experience import Experience
from apps.portfolio.serializers.experience import ExperienceSerializer


class ExperienceView(APIView):
    def get(self, request):
        experience = Experience.objects.all()
        serializer = ExperienceSerializer(experience, many=True)
        return Response(serializer.data)
