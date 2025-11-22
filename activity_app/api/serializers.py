from rest_framework import serializers
from ..models import Activity
from profile_app.api.serializers import UserProfileDetailsSerializer
from user_app.api.serializers import UserSerailizer
class CreateActivitySerializer(serializers.ModelSerializer):
    contact = serializers.PrimaryKeyRelatedField(read_only=True)
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Activity
        fields = [
            "id",
            "contact",
            "customer",
            "user",
            "description",
            "type",
            "date",
        ] 

class ActivityListSerializer(serializers.ModelSerializer):
    contact = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()
    user = UserSerailizer(read_only=True)

    class Meta:
        model = Activity
        fields = [
            "id",
            "contact",
            "customer",
            "user",
            "description",
            "type",
            "date",
        ] 


    def get_contact(self, obj):
            if obj:
                contact = {
                    "id": obj.contact.id, 
                    "name": obj.contact.name,
                    }
                return contact 
            
    def get_customer(self, obj):
            if obj:
                customer = {
                    "id": obj.customer.id,
                    "companyname": obj.customer.companyname,
                }
                return customer