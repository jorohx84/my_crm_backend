from django.db import models
from profile_app.models import UserProfile
from customer_app.models import Customer
from simple_history.models import HistoricalRecords

class Task(models.Model):
    STATE_TYPE = [
        ('undone', "Undone"),
        ('in_progress', "In Progress"),
        ('under_review', "Under Review"),
        ('done', "Done"),
        ('released', 'Released'),
        ('closed', 'Closed')
]

    PRIO_TYPE = [
        ('low', "Low"),
        ('mid', "Mid"),
        ('high', "High"),
    ]
   
    title = models.CharField(max_length=255)
    description = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_tasks")
    assignee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="assigned_tasks")
    state = models.CharField(max_length=25, choices=STATE_TYPE, default="undone")
    comments = models.JSONField(default=list)
    priority = models.CharField(max_length=25, choices=PRIO_TYPE, default="low")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='review_tasks')
    completed_at = models.DateTimeField(null=True, blank=True)
    log = models.JSONField(default=list, blank=True)
    subtasks = models.JSONField(default=list, null=True, blank=True)
    board_position = models.IntegerField(default=0)
    history = HistoricalRecords()


class Comment(models.Model):
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE, related_name="task_comment")
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user_comment")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Log(models.Model):
    log = models.CharField(default='')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task_log")
    logged_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="customer_log")
    new_state = models.CharField()

class Tasktemplate(models.Model):
    title = models.CharField()
    description = models.TextField()
    subtasks = models.JSONField(default=list, null=True, blank=True)