from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import ListCreateContactSerializer, ContactDetailSerializer
from ..models import Contact, Customer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter

class ContactPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "size"
    max_page_size = 100

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ListCreateContactSerializer

    def perform_create(self, serializer):
        customer_id = self.request.data['customer']
        user = self.request.user

        
        if not (user and customer_id):
            raise ValidationError("Customer or user not provided")
        else:
            serializer.save(
                customer_id = customer_id,
                created_by = user
                ), 
      

class ContactListView(generics.ListAPIView):
    serializer_class = ListCreateContactSerializer
    pagination_class = ContactPagination
    filter_backends = [OrderingFilter]
 
    ordering_fields = ['name']
    ordering = ['name']   


    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        queryset = Contact.objects.filter(customer_id=customer_id)
        return queryset
    
class ContactListWrapperView(generics.ListAPIView):
    serializer_class = ListCreateContactSerializer
    filter_backends = [OrderingFilter]
 
    ordering_fields = ['name']
    ordering = ['name']   


    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        queryset = Contact.objects.filter(customer_id=customer_id)
        return queryset
    

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactDetailSerializer

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(
            updated_by = user
        )

class ContactSearchView(APIView):
    def get(self, request, field, value, id):
        tenant = request.user.tenant
        customer_id = id
        if not value:
            return Response({"detail": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Prüfen, ob das Feld im Modell existiert, um Fehler zu vermeiden
        valid_fields = [f.name for f in Contact._meta.get_fields()]
        if field not in valid_fields:
            return Response({"detail": f"Invalid search field: {field}"}, status=status.HTTP_400_BAD_REQUEST)
     
        # Dynamische Filterung
        filter_kwargs = {f"{field}__icontains": value}
        queryset = Contact.objects.filter(customer_id=customer_id)
        results = queryset.filter(customer__tenant=tenant, **filter_kwargs)
    
        serialized_results = ListCreateContactSerializer(results, many=True).data

        return Response({
            "results": serialized_results
        })