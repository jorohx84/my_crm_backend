from django.urls import path
from .views import GlobalSearchView

urlpatterns = [
    path('search/<str:input>/', GlobalSearchView.as_view(), name="global-search"),

    # path('list-count/<str:list>/', CountListView.as_view(), name="count-list"),
]