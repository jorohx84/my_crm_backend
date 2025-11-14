from django.urls import path
from .views import CreateActivityView, ActivityContactListView

urlpatterns = [
    path('activities/', CreateActivityView.as_view(), name="activity-create" ),
    path('activities/<int:contact_id>/', ActivityContactListView.as_view(), name="activity-contact" ),
]