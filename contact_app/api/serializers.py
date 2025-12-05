from rest_framework import serializers
from ..models import Contact
from user_app.api.serializers import UserSerailizer
from customer_app.api.serializers import CustomerDetailSerializer
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
    customer = CustomerDetailSerializer(read_only=True)
    created_by =UserSerailizer(read_only=True)
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



class ContactSearchSerializer(serializers.ModelSerializer):
    customer = CustomerDetailSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "customer",
        ]