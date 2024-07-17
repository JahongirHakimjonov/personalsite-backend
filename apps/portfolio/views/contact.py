from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.portfolio.models.contact import ContactInfo
from apps.portfolio.serializers.contact import ContactInfoSerializer


class ContactInfoView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Get contact information",
        responses={200: ContactInfoSerializer()},
    )
    def get(self, request):
        contact_info = ContactInfo.objects.first()
        serializer = ContactInfoSerializer(contact_info)
        return Response(serializer.data)
