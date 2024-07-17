from rest_framework.response import Response
from rest_framework.views import APIView

from apps.portfolio.models.education import Education
from apps.portfolio.serializers.education import EducationSerializer


class EducationView(APIView):
    def get(self, request):
        education = Education.objects.all()
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data)
