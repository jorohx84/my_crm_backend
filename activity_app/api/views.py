from rest_framework import generics
from .serializers import CreateActivitySerializer, ActivityListSerializer, UpdateActivitySerializer
from ..models import Activity

class CreateActivityView(generics.CreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = CreateActivitySerializer

    def perform_create(self, serializer):
        created_by = self.request.user
        customer_id = self.request.data['customer']
        contact_id = self.request.data['contact']

        serializer.save(
            created_by = created_by,
            customer_id = customer_id,
            contact_id = contact_id
        )

class ActivityContactListView(generics.ListAPIView):
    serializer_class = ActivityListSerializer

    def get_queryset(self):
        contact_id = self.kwargs['contact_id']
        queryset = Activity.objects.filter(contact_id=contact_id)
        return queryset
    
class ActivityCustomerListView(generics.ListAPIView):
    serializer_class = ActivityListSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        queryset = Activity.objects.filter(customer_id=customer_id)
        return queryset
    
class ActitityUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all() 
    serializer_class = UpdateActivitySerializer
