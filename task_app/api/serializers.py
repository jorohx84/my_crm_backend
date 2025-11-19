from rest_framework import serializers
from ..models import Task, Comment, Log, Tasktemplate
from profile_app.models import UserProfile
from profile_app.api.serializers import UserProfileDetailsSerializer
from customer_app.models import Customer

class CreateTaskSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(read_only=True)
    parent = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Task
        fields = [
            "id",
            "parent",
            "title",
            "description",
            "customer",
            "assignee",
            "state",
            "priority",
            "created_at",
            "due_date",
            "reviewer",
            "log",
            "checklist",
        ]
        read_only_fields = [
            "id", 
            "created_at", 
            "reviewer",
           
            ]

 
class TaskListSerializer(serializers.ModelSerializer):
    reviewer = UserProfileDetailsSerializer(read_only=True)
    assignee = UserProfileDetailsSerializer(read_only=True)
    parent = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "parent",
            "title",
            "description",
            "customer",
            "assignee",
            "state",
            "priority",
            "created_at",
            "due_date",
            "reviewer",
            "checklist",
            "board_position",
        ]

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
        ]

class TaskCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "companyname",
        ]


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "customer",
            "assignee",
            "state",
            "priority",
            "created_at",
            "due_date",
            "reviewer",
            "log",
            "checklist",
            "board_position",
           
        ]

class CreateCommentSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    task = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "task", "created_at", "creator"]


class ListCommentSerializer(serializers.ModelSerializer):
    creator = UserProfileDetailsSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "creator", "created_at", "task"]
        

class SingleTaskSerializer(serializers.ModelSerializer):
    reviewer = UserProfileDetailsSerializer(read_only=True)
    assignee = UserProfileDetailsSerializer(read_only=True)
    customer = TaskCustomerSerializer(read_only=True)
    comments = ListCommentSerializer( source="task_comment", many=True, read_only=True)
    parent = ParentSerializer(read_only=True)
    class Meta:
        model = Task
        fields = [
            "id",
            "parent",
            "title",
            "description",
            "customer",
            "assignee",
            "state",
            "priority",
            "created_at",
            "due_date",
            "reviewer",
            "comments",
            "log",
            "checklist",
            
        ]



class LogCreateSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    updated_by = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Log
        fields = [
            "id",
            "log",
            "task",
            "logged_at",
            "updated_by",
            "new_state",
           
        ]
        


class LogListSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    updated_by = UserProfileDetailsSerializer(read_only=True)

    class Meta:
        model = Log
        fields = [
            "id",
            "log",
            "task",
            "logged_at",
            "updated_by",
            "new_state",
         
        ]

class CreateTaskTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasktemplate
        fields =[
            "id",
            "title",
            "description",
            "checklist",
        ]