from rest_framework import generics, status
from rest_framework.views import APIView 
from .serializers import NotificationSerializer
from ..models import Notification
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime




class NotificationCreateView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer



class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Notification.objects.filter(recipient_id=user_id)
        return queryset


class NotificationUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Notification.objects.all()
    serializer_class = NotificationSerializer


class NewMessagesCountView(APIView):

    def get(self, request):
        user = request.user
    

        messages = Notification.objects.filter(recipient_id=user.id, is_read=False)


        count = messages.count()
        return Response({
            "count": count,
        }, status=status.HTTP_200_OK)