from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.portfolio.models.support import Support
from apps.portfolio.serializers.support import SupportSerializer


class SupportView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = timezone.now().replace(hour=23, minute=59, second=59, microsecond=999999)

        messages_count = Support.objects.filter(
            email=request.data["email"],
            created_at__range=(today_start, today_end)
        ).count()

        if messages_count >= 3:
            return Response({"error": "You can only send 3 messages per day."}, status=status.HTTP_400_BAD_REQUEST)

        support = Support.objects.create(
            full_name=request.data["full_name"],
            email=request.data["email"],
            message=request.data["message"],
        )
        serializer = SupportSerializer(support)
        return Response(serializer.data)
