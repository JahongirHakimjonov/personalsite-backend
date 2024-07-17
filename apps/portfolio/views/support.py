from rest_framework.response import Response
from rest_framework.views import APIView

from apps.portfolio.models.support import Support
from apps.portfolio.serializers.support import SupportSerializer


class SupportView(APIView):
    def post(self, request):
        support = Support.objects.create(
            full_name=request.data["full_name"],
            email=request.data["email"],
            message=request.data["message"],
        )
        serializer = SupportSerializer(support)
        return Response(serializer.data)
