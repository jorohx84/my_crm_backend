from rest_framework import generics, status
from .serializers import CreateTaskSerializer, TaskListSerializer
from ..models import Task

class CreateTaskView(generics.CreateAPIView):
    queryset=Task.objects.all()
    serializer_class=CreateTaskSerializer
 
    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user.userprofile)


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer

    def get_queryset(self):
        customer_id=self.kwargs.get('customer_id')
        queryset = Task.objects.filter(customer_id=customer_id)
        return queryset