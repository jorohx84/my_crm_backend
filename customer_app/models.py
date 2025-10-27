from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    companyname = models.CharField(max_length=255) 
    street = models.CharField(max_length=255) 
    areacode = models.CharField(max_length=25)
    city = models.CharField(max_length=255) 
    country = models.CharField(max_length=255) 
    email = models.CharField(max_length=255) 
    phone = models.CharField(max_length=25) 
    website = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_createdby")
    is_activ = models.BooleanField(blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lastContact = models.DateTimeField(blank=True, null=True)
    assignedTo = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="customer_assigned", null=True)
    notes = models.TextField( blank=True, null=True, default="")
    description = models.TextField(blank=True, null=True, default="")
    revenue = models.IntegerField( blank=True, null=True, default=0)
    paymentTerms = models.CharField( blank=True, null=True, default="")
    insideSales = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="customer_insidesales", null=True)
    outsideSales = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="customer_outsidesales", null=True)

    def __str__(self):
        return self.companyname
