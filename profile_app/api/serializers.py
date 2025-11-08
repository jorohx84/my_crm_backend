from rest_framework import serializers
from ..models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    fullname = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ["id", "fullname", "user", "first_name", "last_name", "email", "tel", "last_logout", "last_inbox_check"]
        
    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}"