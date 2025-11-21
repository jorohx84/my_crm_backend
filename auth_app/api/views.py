from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import ResgistrationSerializer, LoginSerializer, resetPasswortSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from account_app.utils import send_set_password_email, send_manual_reset_password_email
from django_rq import enqueue
User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    
    serializer_class = ResgistrationSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, created = Token.objects.get_or_create(user=user)

        enqueue(send_set_password_email, user.pk)

        return Response({
            "token": token.key,
            "username": user.username,
            "email": user.email,
            "tenant": user.tenant.id,
            "user_id": user.id,
         }, status=status.HTTP_201_CREATED)
    
     



class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer
    authentication_classes = [TokenAuthentication]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, create = Token.objects.get_or_create(user=user)
    

        return Response({
            "token": token.key,
            "username": user.username,
            "email": user.email,
            "tenant": user.tenant.id,
            "user_id": user.id,
         }, status=status.HTTP_200_OK)
    

class LogoutView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            # Token löschen (User ist durch Token authentifiziert)
            request.user.auth_token.delete()
        except Token.DoesNotExist:
            pass

        return Response({"detail": "Logged out successfully"}, status=status.HTTP_200_OK)
    

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = resetPasswortSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uidb64 = serializer.validated_data['uid']
        token = serializer.validated_data['token']
        new_password = serializer.validated_data['password']

        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            return Response({"detail": "invalid link."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not default_token_generator.check_token(user, token):
            return Response({"detail": "invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        user.is_active=True
        user.save()

        return Response({"detail": "password reset successfully"}, status=status.HTTP_200_OK)
    


class AdminResetPasswordView(APIView):
    # permission_classes = [permissions.IsAdminUser]  # nur Admins dürfen das ausführen

    def post(self, request):
        user_id = request.data.get("user_id")
        print(user_id)
        if not user_id:
            return Response({"detail": "user_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Job in RQ Queue stellen (async Email)
        enqueue(send_manual_reset_password_email, user.pk)
        
        return Response({"detail": f"Password reset email sent to {user.email}"}, status=status.HTTP_200_OK)
