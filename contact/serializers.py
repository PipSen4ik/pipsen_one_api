from rest_framework import serializers
from .models import ContactMessage

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Имя должно быть не менее 2 символов.")
        return value.strip()

    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Сообщение должно быть не менее 10 символов.")
        return value.strip()