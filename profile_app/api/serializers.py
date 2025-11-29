from rest_framework import serializers
from ..models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    fullname = serializers.SerializerMethodField()
    tenant = serializers.SerializerMethodField()  
    class Meta:
        model = UserProfile
        fields = ["id", "fullname", "user", "tenant", "first_name", "last_name", "email", "phone", "last_logout", "last_inbox_check", "color"]
        
    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
    def get_tenant(self, obj):
        # Gibt nur die Tenant-ID zurück, None falls kein Tenant
        return obj.user.tenant.id if obj.user.tenant else None
    
    
class UserProfileDetailsSerializer(serializers.ModelSerializer):
    fullname=serializers.SerializerMethodField()
    initials = serializers.SerializerMethodField()
    
    class Meta:
        model = UserProfile
        fields = ["id","fullname", "email", "phone", "department", "initials", "color"]
        read_only_fields = ["first_name", "last_name"] 

    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_initials(self, obj):
        return (obj.first_name[:1] + obj.last_name[:1]).upper()
