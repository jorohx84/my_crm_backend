from django.urls import path
from .views import CustomerListCreateView, SingleCustomerView,CustomerSearchView
urlpatterns = [
    path('customers/',CustomerListCreateView.as_view(), name="customer-list"),
    path('customers/<int:pk>/', SingleCustomerView.as_view(), name="customer-detail"),
    path('customers/search/<str:field>/<str:value>/', CustomerSearchView.as_view(), name="customer-search"),
]