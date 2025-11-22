from django.urls import path
from .views import SingleProfileView, ProfileListView, ProfileSearchView
urlpatterns = [
    path('profile/', ProfileListView.as_view(), name="profile"),
    path('profile/<int:user_id>/', SingleProfileView.as_view(), name="profile-detail"),
    path ('profile/search/<str:input>/', ProfileSearchView.as_view(), name="profile-search"),
    
]