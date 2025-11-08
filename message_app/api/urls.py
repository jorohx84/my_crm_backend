from django.urls import path
from .views import SytemMessageCreateView, SystemMessageListView, NewMessagesCountView, SystemMessageUpdateView

urlpatterns = [
path('system-messages/', SytemMessageCreateView.as_view(), name="system-message"),
path('system-messages/user/<int:user_id>/', SystemMessageListView.as_view(),name="system-message-list" ),
path('messages/count/', NewMessagesCountView.as_view(), name="messages-count"),
path('system-messages/<int:pk>/', SystemMessageUpdateView.as_view(), name="system-message-detail"),
]