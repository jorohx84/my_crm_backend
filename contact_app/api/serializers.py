from rest_framework import serializers
from ..models import Contact
from profile_app.api.serializers import UserProfileDetailsSerializer

class ListCreateContactSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    created_by =serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Contact
        fields =[
            "id",
            "customer",
            "name",
            "function",
            "position",
            "department",
            "phone",
            "email",
            "created_by"
        ]


class ContactDetailSerializer(serializers.ModelSerializer):
    # customer = serializers.PrimaryKeyRelatedField(read_only=True)
    created_by =serializers.SerializerMethodField()
    updated_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Contact
        fields =[
            "id",
            "customer",
            "name",
            "function",
            "position",
            "department",
            "phone",
            "email",
            "created_by",
            "newsletter_opt_in",
            "notes",
            "updated_at",
            "updated_by",
        ]

    def get_created_by(self, obj):
        return UserProfileDetailsSerializer(obj.created_by.userprofile).data