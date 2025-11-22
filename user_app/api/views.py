from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerailizer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListView(generics.ListAPIView):
    
    serializer_class = UserSerailizer

    def get_queryset(self):
        tenant_id = self.request.user.tenant
        users = User.objects.filter(tenant_id=tenant_id, is_staff=False)
        return users
    
class SingleUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerailizer


class UserSearchView(APIView):
 def get(self, request, input):
    query = input
    if not query:
        return Response({"detail": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)
    tenant = self.request.user.tenant
    search_result = User.objects.filter(tenant=tenant).filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)).annotate(fullname=Concat("first_name", Value(' '), 'last_name')).values("id", "fullname", "email",)

    return Response(list(search_result))
 

class CheckEmailView(generics.ListAPIView):
    serializer_class = UserSerailizer

    def get_queryset(self):
        email = self.kwargs['email']
        tenant=self.request.user.tenant
        user = User.objects.filter(email=email, tenant=tenant)
        return user