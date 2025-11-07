from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateTaskSerializer, TaskListSerializer, SingleTaskSerializer, CreateCommentSerializer, ListCommentSerializer, TaskUpdateSerializer
from ..models import Task, Comment
from profile_app.models import UserProfile
from django.shortcuts import get_object_or_404
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

class SubtaskCountView(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'No Task Found'}, status=status.HTTP_404_NOT_FOUND)

        subtasks = task.subtasks
        total_count = subtasks.count()
        completed_subtasks = subtasks.filter(state='done')
        completed_count = completed_subtasks.count()

        return Response({
            "total_count": total_count,
            "completed_count":completed_count 
             })
          

class TaskBoardAssigneeView(generics.ListAPIView):
    serializer_class = TaskListSerializer 

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        tasks = Task.objects.filter(assignee_id=user_id)
        return tasks
    
class TaskBoardReviewerView(generics.ListAPIView):
    serializer_class=TaskListSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        tasks = Task.objects.filter(reviewer_id=user_id)
        return tasks
    

class TaskBoardRealesesView(generics.ListAPIView):
    serializer_class=TaskListSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        tasks = Task.objects.filter(reviewer_id=user_id, state='done')
        return tasks