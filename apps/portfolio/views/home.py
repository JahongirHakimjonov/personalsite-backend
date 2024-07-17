from rest_framework.response import Response
from rest_framework.views import APIView

from apps.portfolio.models.home import Home
from apps.portfolio.serializers.home import HomeSerializer


class HomeView(APIView):
    def get(self, request):
        home = Home.objects.first()
        serializer = HomeSerializer(home)
        return Response(serializer.data)
