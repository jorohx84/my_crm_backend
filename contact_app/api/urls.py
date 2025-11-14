from django.urls import path
from .views import ContactCreateView, ContactListView, ContactDetailView


urlpatterns = [
    path('contacts/', ContactCreateView.as_view(), name="contact-create" ),
    path('contacts/<int:customer_id>/', ContactListView.as_view(), name="contactlist" ),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name="contact-detail" ),

]