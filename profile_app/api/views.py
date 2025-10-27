from rest_framework import generics, status
from .serializers import UserProfileSerializer
from ..models import UserProfile

class ProfileListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class SingleProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CheckEmailView(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        email = self.kwargs['email']
        profile = UserProfile.objects.filter(email=email)
        return profile