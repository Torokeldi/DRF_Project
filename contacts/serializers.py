from rest_framework import serializers
from .models import contact

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, allow_blank=True)
    class Meta:
        model = contact
        fields = '__all__'

    def validate_name(self, value):
        if value.strip() == "":
            raise serializers.ValidationError("Аты бош болбошу керек")
        return value

    def validate_phone(self, value):
        if len(value) < 12:
            raise serializers.ValidationError("Номер 12 сандан кыска болбош керек")
        return value
