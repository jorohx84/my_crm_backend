from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer_app.models import Customer
from task_app.models import Task
from profile_app.models import UserProfile
from contact_app.models import Contact
from activity_app.models import Activity
from activity_app.api.serializers import ActivityListSerializer
from django.contrib.auth import get_user_model
from user_app.api.serializers import UserSerailizer
from customer_app.api.serializers import CustomerSerializer
from contact_app.api.serializers import ContactSearchSerializer
User = get_user_model()
class GlobalSearchView(APIView):
    def get(self, request, input):
        query = input
        if not query:
            return Response({"detail": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        tenant = request.user.tenant

        user_results = User.objects.filter(tenant=tenant).filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query))

        task_results = Task.objects.filter(customer__tenant=tenant).filter(Q(title__icontains=query) | Q(description__icontains=query)).values("id", "title", "description", "customer")

        customer_results = Customer.objects.filter(tenant=tenant).filter(Q(companyname__icontains=query)).values("id", "companyname", "phone", "email", "areacode", "city")

        contact_results = Contact.objects.filter(customer__tenant=tenant).filter(Q(name__icontains=query) | (Q(email__icontains=query))).values("id", "name", "email", "phone", "department", "customer")

        # hier mit Serilaizer
        user_data = UserSerailizer(user_results, many=True).data

        return Response({
            "members": list(user_data),
            "tasks": list(task_results),
            "customers": list (customer_results),
            "contacts": list(contact_results),
        })
    

    

# class CountListView(APIView):
#     def get(self, request, list):
#         if list == 'customers':
#             Model = Customer
#         tenant = self.request.user.tenant

#         count = Model.objects.filter(tenant=tenant).count()

#         return Response({"count":count})

class ContactSearchView(APIView):
    def get(self, request, input):
        if not input:
            return Response({"detail": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)
        tenant = request.user.tenant

        query = Contact.objects.filter(customer__tenant=tenant)

        results = query.filter(Q(name__icontains=input))

        data = ContactSearchSerializer(results, many=True).data

        return Response(list(data))
           
