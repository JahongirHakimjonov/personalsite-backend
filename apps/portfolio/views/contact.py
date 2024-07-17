from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.portfolio.models.contact import ContactInfo
from apps.portfolio.serializers.contact import ContactInfoSerializer


class ContactInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        contact_info = ContactInfo.objects.first()
        serializer = ContactInfoSerializer(contact_info)
        return Response(serializer.data)
