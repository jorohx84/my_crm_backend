from rest_framework import serializers
from ..models import Task
from profile_app.models import UserProfile

class CreateTaskSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(read_only=True)
    
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

        ]
        read_only_fields = [
            "id", 
            "created_at", 
            "reviewer"
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
        ]
