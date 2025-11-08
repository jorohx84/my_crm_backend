from rest_framework import generics, status
from rest_framework.views import APIView 
from .serializers import SytemMessageSerializer
from ..models import SystemMessage
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime




class SytemMessageCreateView(generics.CreateAPIView):
    queryset = SystemMessage.objects.all()
    serializer_class = SytemMessageSerializer



class SystemMessageListView(generics.ListAPIView):
    serializer_class = SytemMessageSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = SystemMessage.objects.filter(recipient_id=user_id)
        return queryset


class SystemMessageUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset= SystemMessage.objects.all()
    serializer_class = SytemMessageSerializer


class NewMessagesCountView(APIView):

    def get(self, request):
        user = request.user
    

        messages = SystemMessage.objects.filter(recipient_id=user.id, is_read=False)


        count = messages.count()
        return Response({
            "count": count,
        }, status=status.HTTP_200_OK)