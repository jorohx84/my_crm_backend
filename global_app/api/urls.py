from django.urls import path
from .views import GlobalSearchView

urlpatterns = [
    path('search/<str:input>/', GlobalSearchView.as_view(), name="global-search"),
]