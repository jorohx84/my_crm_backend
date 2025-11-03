from rest_framework import serializers
from ..models import Task, Comment
from profile_app.models import UserProfile
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
            "type",
        ]
        read_only_fields = [
            "id", 
            "created_at", 
            "reviewer",
           
            ]
        
class ReviewerAssigneeSerializer(serializers.ModelSerializer):
    fullname=serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ["id", "fullname", "email"]
        read_only_fields = ["first_name", "last_name"] 

    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}"

 
class TaskListSerializer(serializers.ModelSerializer):
    reviewer = ReviewerAssigneeSerializer(read_only=True)
    assignee = ReviewerAssigneeSerializer(read_only=True)
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
            "type",
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
        ]

class CreateCommentSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    task = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "task", "created_at", "creator"]


class ListCommentSerializer(serializers.ModelSerializer):
    creator = ReviewerAssigneeSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "creator", "created_at", "task"]
        

class SingleTaskSerializer(serializers.ModelSerializer):
    reviewer = ReviewerAssigneeSerializer(read_only=True)
    assignee = ReviewerAssigneeSerializer(read_only=True)
    customer = TaskCustomerSerializer(read_only=True)
    comments = ListCommentSerializer( source="task_comment", many=True, read_only=True)
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
            "comments",
            "log",
            "type",
        ]



class SubtaskListSerializer(serializers.ModelSerializer):
    reviewer = ReviewerAssigneeSerializer(read_only=True)
    assignee = ReviewerAssigneeSerializer(read_only=True)
    task=serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "task",
            "title",
            "description",
            "customer",
            "assignee",
            "state",
            "priority",
            "created_at",
            "due_date",
            "reviewer",
            "type",
        ]


