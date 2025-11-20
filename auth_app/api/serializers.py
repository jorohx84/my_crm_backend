from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from profile_app.models import UserProfile

User = get_user_model()

class ResgistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "repeated_password"]

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "User with this email already excist"})
        if attrs['password'] != attrs['repeated_password']:
            raise serializers.ValidationError({"repeated_password": "Password do not match"})
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('repeated_password')
        username = validated_data.get('email')
        request_user = self.context['request'].user
        tenant = request_user.tenant
        user = User.objects.create(username=username, tenant=tenant, **validated_data)
        user.set_password(password)
        user.save()

        UserProfile.objects.create(
            user = user,
            email = user.email,
            first_name = user.first_name,
            last_name = user.last_name,
            phone = '',
        )
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate (username=username, password=password)

        if not user:
            raise serializers.ValidationError({"error": "Invalid username or password"})
        attrs["user"]=user

        return attrs