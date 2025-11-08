from django.urls import path
from .views import SytemMessageCreateView, SystemMessageListView

urlpatterns = [
path('system-messages/', SytemMessageCreateView.as_view(), name="system-message"),
path('system-messages/<int:user_id>/', SystemMessageListView.as_view(),name="system-message-list" )
]