
from rest_framework import serializers
from django.contrib.auth import get_user_model
from profile_app.api.serializers import UserProfileDetailsSerializer
User = get_user_model()



class UserSerailizer(serializers.ModelSerializer):
    profile = UserProfileDetailsSerializer(read_only=True)
    class Meta:
        model = User
        fields = [
            "id",
            "profile"
        ]

