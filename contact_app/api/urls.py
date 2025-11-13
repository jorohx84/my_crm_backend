from django.urls import path
from .views import ContactCreateView, ContactListView


urlpatterns = [
    path('contacts/', ContactCreateView.as_view(), name="contact-create" ),
    path('contacts/<int:customer_id>/', ContactListView.as_view(), name="contactlist" ),
]