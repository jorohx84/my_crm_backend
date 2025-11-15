from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer_app.models import Customer
from task_app.models import Task
from profile_app.models import UserProfile
from contact_app.models import Contact

class GlobalSearchView(APIView):
    def get(self, request, input):
        query = input
        if not query:
            return Response({"detail": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_results = UserProfile.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)).values("id","first_name", "last_name", "email")

        task_results = Task.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).values("id", "title", "description", "customer", "type")

        customer_results = Customer.objects.filter(Q(companyname__icontains=query)).values("id", "companyname", "phone", "email", "areacode", "city")

        contact_results = Contact.objects.filter(Q(name__icontains=query) | (Q(email__icontains=query))).values("id", "name", "email", "phone", "department", "customer")

        return Response({
            "members": list(user_results),
            "tasks": list(task_results),
            "customers": list (customer_results),
            "contacts": list(contact_results),
        })