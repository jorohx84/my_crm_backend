from rest_framework import generics, status
from .serializers import CustomerSerializer, SingleCustomerSerializer
from ..models import Customer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class = CustomerSerializer

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
