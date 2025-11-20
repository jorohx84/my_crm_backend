from django.urls import path
from .views import SingleProfileView, CheckEmailView, ProfileListView, ProfileSearchView
urlpatterns = [
    path('profile/', ProfileListView.as_view(), name="profile"),
    path('profile/<int:user_id>/', SingleProfileView.as_view(), name="profile-detail"),
    path('email-check/<str:email>', CheckEmailView.as_view(), name="email-check"),
    path ('profile/search/<str:input>/', ProfileSearchView.as_view(), name="profile-search"),
    
]