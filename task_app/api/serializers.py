from rest_framework import serializers
from ..models import Task, Comment, Log, Tasktemplate
from customer_app.models import Customer
from customer_app.api.serializers import CustomerDetailSerializer
from user_app.api.serializers import UserSerailizer
class CreateTaskSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
   
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "customer",
            "state",
            "priority",
            "created_at",
            "due_date",
            "reviewer",
            "created_by",
            "log",
            "subtasks",
            "members"
        ]
        read_only_fields = [
            "id", 
            "created_at", 
            "reviewer",
           
            ]

 
class TaskListSerializer(serializers.ModelSerializer):
    reviewer = UserSerailizer(read_only=True)
    customer = CustomerDetailSerializer(read_only=True)
    members = UserSerailizer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "customer",
            "state",
            "priority",
            "created_at",
            "due_date",
            "reviewer",
            "subtasks",
            "board_position",
            "members",
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
            "state",
            "priority",
            "created_at",
            "due_date",
            "reviewer",
            "log",
            "subtasks",
            "board_position",
            "members",
        ]

class CreateCommentSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    task = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "task", "created_at", "creator"]


class ListCommentSerializer(serializers.ModelSerializer):
    creator = UserSerailizer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "creator", "created_at", "task"]
        
class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text"]  


class SingleTaskSerializer(serializers.ModelSerializer):
    reviewer = UserSerailizer(read_only=True)
    customer = TaskCustomerSerializer(read_only=True)
    # comments = ListCommentSerializer( source="task_comment", many=True, read_only=True)
    members = UserSerailizer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "customer",
            "state",
            "priority",
            "created_at",
            "due_date",
            "reviewer",
            # "comments",
            "log",
            "subtasks",
            "members",
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
            "type",
            "subtask",
        ]
        


class LogListSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    updated_by = UserSerailizer(read_only=True)

    class Meta:
        model = Log
        fields = [
            "id",
            "log",
            "task",
            "logged_at",
            "updated_by",
            "new_state",
            "type",
            "subtask",
        ]

class CreateTaskTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasktemplate
        fields =[
            "id",
            "title",
            "description",
            "subtasks",
        ]