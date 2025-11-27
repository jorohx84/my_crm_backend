from django.db.models import Q
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from .serializers import CustomerSerializer, SingleCustomerSerializer
from ..models import Customer

class CustomerPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "size"
    max_page_size = 100

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomerPagination
    filter_backends = [OrderingFilter]
 
    ordering_fields = ['companyname']
    ordering = ['companyname']   

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            tenant=self.request.user.tenant
            )

    def get_queryset(self):
        tenant_id = self.request.user.tenant
        queryset = Customer.objects.filter(is_activ=True, tenant_id=tenant_id)
        return queryset

class SingleCustomerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = SingleCustomerSerializer

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


