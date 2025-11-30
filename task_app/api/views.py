from django.db.models import Q
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateTaskSerializer, TaskListSerializer, SingleTaskSerializer, CreateCommentSerializer, ListCommentSerializer, TaskUpdateSerializer, LogCreateSerializer, LogListSerializer, CreateTaskTemplateSerializer
from ..models import Task, Comment, Log, Tasktemplate
from profile_app.models import UserProfile
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
class CreateTaskView(generics.CreateAPIView):
    queryset=Task.objects.all()
    serializer_class=CreateTaskSerializer
 
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(
            reviewer=user,
            created_by=user,
            )


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer

    def get_queryset(self):
        customer_id=self.kwargs.get('customer_id')
        filter = self.kwargs.get('filter')
        if filter== 'open':

            queryset = Task.objects.filter(customer_id=customer_id).exclude(state__in=['released', 'closed'])
        else: 
            queryset = Task.objects.filter(customer_id=customer_id, state=filter)
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
            creator=self.request.user, 
            task_id=task_id
            )


class CommentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=ListCommentSerializer


          

class TaskBoardAssigneeView(generics.ListAPIView):
    serializer_class = TaskListSerializer 

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        tasks = Task.objects.filter( Q(members__id=user_id)).exclude(state__in=['closed']).distinct()
        return tasks
    


    
class TaskBoardReviewerView(generics.ListAPIView):
    serializer_class=TaskListSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        tasks = Task.objects.filter(reviewer_id=user_id).exclude(state__in=['closed'])
        return tasks
    

class TaskBoardRealesesView(generics.ListAPIView):
    serializer_class=TaskListSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        tasks = Task.objects.filter(reviewer_id=user_id, state='done')
        return tasks
    
class CreateLogView(generics.CreateAPIView):
    queryset=Log.objects.all()
    serializer_class = LogCreateSerializer

    def perform_create(self, serializer):  
        task_id = self.request.data['task']
        serializer.save(
            updated_by = self.request.user,
            task_id = task_id 
        )

class LogListView(generics.ListAPIView):
    serializer_class = LogListSerializer
    
    def get_queryset(self):
        task_id = self.kwargs['task_id']
        logs = Log.objects.filter(task_id=task_id)
        return logs

class CreateTaskTemplateView(generics.ListCreateAPIView):
    queryset = Tasktemplate.objects.all()
    serializer_class = CreateTaskTemplateSerializer

class TaskTemplateUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasktemplate.objects.all()
    serializer_class = CreateTaskTemplateSerializer