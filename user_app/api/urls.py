from django.urls import path
from .views import UserListView, SingleUserView, UserSearchView, CheckEmailView

urlpatterns = [
path('users/', UserListView.as_view(), name="users"),
path('users/<int:pk>/', SingleUserView.as_view(), name="user-details"),
path ('users/search/<str:input>/', UserSearchView.as_view(), name="user-search"),
path ('users/email-check/<str:email>/', CheckEmailView.as_view(), name="email-check"),
]