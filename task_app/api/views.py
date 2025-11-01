from rest_framework import generics, status
from .serializers import CreateTaskSerializer, TaskListSerializer, SingleTaskSerializer, CreateCommentSerializer, ListCommentSerializer, CreateSubtaskSerializer
from ..models import Task, Comment, Subtask

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
    

class SingleTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = SingleTaskSerializer





class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer

    def perform_create(self, serializer):
        task_id=self.request.data["task"]
        serializer.save(
            creator=self.request.user.userprofile, 
            task_id=task_id
            )

class CommentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=ListCommentSerializer


class SubtaskCreatetView(generics.ListCreateAPIView):
    queryset = Subtask.objects.all()
    serializer_class = CreateSubtaskSerializer

    def perform_create(self, serializer):
        task_id = self.request.data.get('task')
        task = Task.objects.get(id=task_id)
        serializer.save(
            reviewer = self.request.user.userprofile,
            task=task
        )