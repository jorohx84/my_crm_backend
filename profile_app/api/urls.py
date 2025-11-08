from django.urls import path
from .views import SingleProfileView, CheckEmailView, ProfileListView
urlpatterns = [
    path('profile/', ProfileListView.as_view(), name="profile"),
    path('profile/<int:pk>/', SingleProfileView.as_view(), name="profile-detail"),
    path('email-check/<str:email>', CheckEmailView.as_view(), name="email-check"),
    
]