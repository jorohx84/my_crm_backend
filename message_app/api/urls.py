from django.urls import path
from .views import NotificationCreateView, NotificationListView, NewMessagesCountView, NotificationUpdateView

urlpatterns = [
path('notifications/', NotificationCreateView.as_view(), name="system-message"),
path('notifications/user/<int:user_id>/', NotificationListView.as_view(),name="system-message-list" ),
path('messages/count/', NewMessagesCountView.as_view(), name="messages-count"),
path('notifications/<int:pk>/', NotificationUpdateView.as_view(), name="system-message-detail"),
]