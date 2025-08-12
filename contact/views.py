from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings
from .email_utils import send_contact_email_notification
from .serializers import ContactSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def send_contact_email(request):
    serializer = ContactSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    contact_message = serializer.save()

    context = {
        'name': contact_message.name,
        'email': contact_message.email,
        'message': contact_message.message,
        'website_url': settings.WEBSITE_URL,
    }
    try:
        send_contact_email_notification(context, contact_message.email)
        return Response({"detail": "Сообщение успешно отправлено"}, status=201)
    except Exception as e:
        return Response({"detail": f"Ошибка при отправке: {e}"}, status=500)