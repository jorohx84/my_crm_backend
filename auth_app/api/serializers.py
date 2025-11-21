from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from profile_app.models import UserProfile
from django.utils.crypto import get_random_string
User = get_user_model()

    
class ResgistrationSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "phone"]

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "User with this email already exists"})
        return attrs

    def create(self, validated_data):
        username = validated_data.get('email')
        phone = validated_data.pop('phone', '')

        request_user = self.context['request'].user
        tenant = request_user.tenant

        raw_password = get_random_string(12)

        user = User.objects.create(
            username=username,
            tenant=tenant,
            **validated_data
        )
        user.phone = phone
        user.set_password(raw_password)
        user.save()

        # UserProfile.objects.create(
        #     user=user,
        #     email=user.email,
        #     first_name=user.first_name,
        #     last_name=user.last_name,
        #     phone=phone
        # )

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

class resetPasswortSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    password = serializers.CharField(min_length=8)