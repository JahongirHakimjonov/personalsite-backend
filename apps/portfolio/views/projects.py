from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.portfolio.models.projects import Project
from apps.portfolio.serializers.projects import ProjectSerializer


class ProjectsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
