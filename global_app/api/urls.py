from django.urls import path
from .views import GlobalSearchView, ContactSearchView

urlpatterns = [
    path('search/global/<str:input>/', GlobalSearchView.as_view(), name="global-search"),
    path('search/contact/<str:input>/', ContactSearchView.as_view(), name="contact-search")
    # path('list-count/<str:list>/', CountListView.as_view(), name="count-list"),
]