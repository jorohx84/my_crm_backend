from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateActivitySerializer, ActivityListSerializer, UpdateActivitySerializer
from ..models import Activity
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django.utils.dateparse import parse_date
from django.utils.timezone import make_aware
import datetime

class CustomerPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "size"
    max_page_size = 100

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
    pagination_class = CustomerPagination
    filter_backends = [OrderingFilter]
 
    ordering_fields = ['date']
    ordering = ['-date']
    def get_queryset(self):
        contact_id = self.kwargs['contact_id']
        queryset = Activity.objects.filter(contact_id=contact_id)
        return queryset
    
class ActivityCustomerListView(generics.ListAPIView):
    serializer_class = ActivityListSerializer
    pagination_class = CustomerPagination
    filter_backends = [OrderingFilter]
 
    ordering_fields = ['date']
    ordering = ['-date']
    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        queryset = Activity.objects.filter(customer_id=customer_id)
        return queryset
    
class ActitityUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all() 
    serializer_class = UpdateActivitySerializer


class ActivitySearchView(APIView):
    def get(self, request, key, id):
        start = request.query_params.get("start")
        end = request.query_params.get("end")
        tenant= self.request.user.tenant

        queryset = Activity.objects.filter(customer__tenant=tenant)
        
        filter_key = f"{key}_id"
        qs = queryset.filter(**{filter_key: id})

        if start:
            start_date = make_aware(datetime.datetime.combine(parse_date(start), datetime.time.min))
            qs = qs.filter(date__gte=start_date)

        if end:
            end_date = make_aware(datetime.datetime.combine(parse_date(end), datetime.time.max))
            qs = qs.filter(date__lte=end_date)

        qs = qs.order_by('-date') 
        
        serialized_results = ActivityListSerializer(qs, many=True).data

        return Response({"result": serialized_results},status=status.HTTP_200_OK)
