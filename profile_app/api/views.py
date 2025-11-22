from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from ..models import UserProfile


class ProfileListView(generics.ListAPIView):
    # queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        tenant_id=self.request.user.tenant
        profiles = UserProfile.objects.filter(user__tenant=tenant_id, user__is_staff=False)
        return profiles


class SingleProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user_id'  # Wichtig für RetrieveUpdateAPIView

    def get(self, request, *args, **kwargs):
        profile = self.get_object()  # nutzt lookup_field automatisch
        serializer = self.get_serializer(profile)
        return Response(serializer.data)


# class CheckEmailView(generics.ListAPIView):
#     serializer_class = UserProfileSerializer

#     def get_queryset(self):
#         email = self.kwargs['email']
#         tenant_id=self.request.user.tenant.id
#         profile = UserProfile.objects.filter(email=email, user__tenant_id=tenant_id)
#         return profile


class ProfileSearchView(APIView):
 def get(self, request, input):
    query = input
    if not query:
        return Response({"detail": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)
    tenant_id = self.request.user.tenant
    search_result = UserProfile.objects.filter(user__tenant=tenant_id).filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)).annotate(fullname=Concat("first_name", Value(' '), 'last_name')).values("id", "fullname", "email", "user")

    return Response(list(search_result))