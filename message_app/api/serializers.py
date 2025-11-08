from rest_framework import serializers
from ..models import SystemMessage
from profile_app.models import UserProfile
class SytemMessageSerializer(serializers.ModelSerializer):
    recipient = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = SystemMessage
        fields = [
            "id",
            "recipient",
            "text",
            "created_at",
            "url",
            "is_read",
        ]