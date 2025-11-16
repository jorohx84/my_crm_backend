from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
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


class ProfileSearchView(APIView):
 def get(self, reuquest, input):
    query = input
    if not query:
        return Response({"detail": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)
    
    search_result = UserProfile.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)).annotate(fullname=Concat("first_name", Value(' '), 'last_name')).values("id", "fullname", "email")

    return Response(list(search_result))