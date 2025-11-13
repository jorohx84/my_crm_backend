from rest_framework import serializers
from ..models import Contact
from profile_app.api.serializers import UserProfileDetailsSerializer

class CreateContactSerializer(serializers.ModelSerializer):
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
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    created_by = UserProfileDetailsSerializer(read_only=True)
    
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
        ]