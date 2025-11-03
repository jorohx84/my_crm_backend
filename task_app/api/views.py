from rest_framework import generics, status
from .serializers import CreateTaskSerializer, TaskListSerializer, SingleTaskSerializer, CreateCommentSerializer, ListCommentSerializer, TaskUpdateSerializer
from ..models import Task, Comment

class CreateTaskView(generics.CreateAPIView):
    queryset=Task.objects.all()
    serializer_class=CreateTaskSerializer
 
    def perform_create(self, serializer):
        parent_id = self.request.data.get('parent')
        serializer.save(
            reviewer=self.request.user.userprofile,
            parent_id=parent_id
            )


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer

    def get_queryset(self):
        customer_id=self.kwargs.get('customer_id')
        
        queryset = Task.objects.filter(customer_id=customer_id, type='task')
        return queryset
    

class SingleTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return TaskUpdateSerializer
        else:
            return SingleTaskSerializer



class CreateTaskCommentView(generics.CreateAPIView):
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


class SubtaskListView(generics.ListAPIView):
    serializer_class=TaskListSerializer

    def get_queryset(self):
        parent_id = self.kwargs['parent_id']
        queryset = Task.objects.filter(parent_id=parent_id, type="subtask")
        return queryset

