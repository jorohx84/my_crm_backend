from django.urls import path
from .views import GlobalSearchView, SearchListView

urlpatterns = [
    path('search/<str:input>/', GlobalSearchView.as_view(), name="global-search"),
    path('search-list/<str:list>/<str:field>/<str:value>/', SearchListView.as_view(), name="customer-search"),
    # path('list-count/<str:list>/', CountListView.as_view(), name="count-list"),
]