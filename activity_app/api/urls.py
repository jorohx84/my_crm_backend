from django.urls import path
from .views import CreateActivityView, ActivityContactListView, ActivityCustomerListView, ActitityUpdateDeleteView

urlpatterns = [
    path('activities/', CreateActivityView.as_view(), name="activity-create" ),
    path('activities/contact/<int:contact_id>/', ActivityContactListView.as_view(), name="activity-contact" ),
    path('activities/customer/<int:customer_id>/', ActivityCustomerListView.as_view(), name="activity-customer" ),
    path('activity/<int:pk>/', ActitityUpdateDeleteView.as_view(), name="activity-edit"),
]