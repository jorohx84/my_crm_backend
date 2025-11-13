from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from .serializers import CreateContactSerializer, ContactDetailSerializer
from ..models import Contact, Customer

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = CreateContactSerializer

    def perform_create(self, serializer):
        customer_id = self.request.data['customer']
        user = self.request.user

        
        if not (user and customer_id):
            raise ValidationError("Customer or user not provided")
        else:
            serializer.save(
                customer_id = customer_id,
                created_by = user.userprofile
                ), 
      

class ContactListView(generics.ListAPIView):
    serializer_class = ContactDetailSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        queryset = Contact.objects.filter(customer_id=customer_id)
        return queryset