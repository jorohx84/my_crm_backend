from rest_framework import serializers
from ..models import Notification
from profile_app.models import UserProfile


class NotificationSerializer(serializers.ModelSerializer):
    recipient = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Notification
        fields = [
            "id",
            "recipient",
            "text",
            "created_at",
            "url",
            "param",
            "is_read",
        ]