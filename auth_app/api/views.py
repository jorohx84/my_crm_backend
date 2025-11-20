from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from .serializers import ResgistrationSerializer, LoginSerializer
from rest_framework.authentication import TokenAuthentication
User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    
    serializer_class = ResgistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, created = Token.objects.get_or_create(user=user)
        print("AUTH HEADER:", request.headers.get("Authorization"))
        print("USER:", request.user)
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