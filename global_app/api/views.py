from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer_app.models import Customer
from task_app.models import Task
from profile_app.models import UserProfile
from contact_app.models import Contact
from django.contrib.auth import get_user_model
from user_app.api.serializers import UserSerailizer
from customer_app.api.serializers import CustomerSerializer
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
    

class SearchListView(APIView):
    def get(self, request, field, value, list):
        tenant = request.user.tenant

        if not value:
            return Response({"detail": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        if list =='customers':
            Model = Customer
            Serialzer = CustomerSerializer

        # Prüfen, ob das Feld im Modell existiert, um Fehler zu vermeiden
        valid_fields = [f.name for f in Customer._meta.get_fields()]
        if field not in valid_fields:
            return Response({"detail": f"Invalid search field: {field}"}, status=status.HTTP_400_BAD_REQUEST)

        # Dynamische Filterung
        filter_kwargs = {f"{field}__icontains": value}
        results = Model.objects.filter(tenant=tenant, **filter_kwargs)

        serialized_results = Serialzer(results, many=True).data

        return Response({
            "results": serialized_results
        })
    

# class CountListView(APIView):
#     def get(self, request, list):
#         if list == 'customers':
#             Model = Customer
#         tenant = self.request.user.tenant

#         count = Model.objects.filter(tenant=tenant).count()

#         return Response({"count":count})