from rest_framework import generics
from .serializers import SytemMessageSerializer
from ..models import SystemMessage

class SytemMessageCreateView(generics.CreateAPIView):
    queryset = SystemMessage.objects.all()
    serializer_class = SytemMessageSerializer



class SystemMessageListView(generics.ListAPIView):
    serializer_class = SytemMessageSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = SystemMessage.objects.filter(recipient_id=user_id)
        return queryset