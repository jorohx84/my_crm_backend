from rest_framework import serializers
from..models import Customer
from django.contrib.auth import get_user_model
from user_app.api.serializers import UserSerailizer
User = get_user_model()

class CustomerSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    tenant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = ["id", 
                  "tenant",
                  "companyname", 
                  "street", 
                  "areacode", 
                  "city", 
                  "country", 
                  "email", 
                  "phone", 
                  "website", 
                  "branch", 
                  "created_by"
                  
                  ]
        

        

class SingleCustomerSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()
    editor = serializers.SerializerMethodField()
    updated_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "companyname",
            "street",
            "areacode",
            "city",
            "country",
            "email",
            "phone",
            "website",
            "branch",
            "is_activ",
            "created_at",
            "description",
            "updated_at",
            "updated_by",
            "lastContact",
            "assignedTo",
            "notes",
            "revenue",
            "paymentTerms",
            "insideSales",
            "outsideSales",
            "creator",
            "editor",
        ]


    def get_creator(self, obj):
        if obj.created_by:
            return f"{obj.created_by.first_name} {obj.created_by.last_name}"
        else: 
            None

    def get_editor(self, obj):
        if obj.updated_by:
            return f"{obj.updated_by.first_name} {obj.updated_by.last_name}"
        

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "companyname"
        ]