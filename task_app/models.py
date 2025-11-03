from django.db import models
from profile_app.models import UserProfile
from customer_app.models import Customer


class Task(models.Model):
    STATE_TYPE = [
        ('undone', "Undone"),
        ('in_progress', "In Progress"),
        ('under_review', "Under Review"),
        ('done', "Done"),
]

    PRIO_TYPE = [
        ('low', "Low"),
        ('mid', "Mid"),
        ('high', "High"),
    ]
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="subtasks")
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
    type= models.CharField(default="task")





# class Subtask(models.Model):
#     STATE_TYPE = [
#         ('undone', "Undone"),
#         ('in_progress', "In Progress"),
#         ('under_review', "Under Review"),
#         ('done', "Done"),
# ]

#     PRIO_TYPE = [
#         ('low', "Low"),
#         ('mid', "Mid"),
#         ('high', "High"),
#     ]
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task_subtasks")
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_subtasks")
#     assignee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="assigned_subtask")
#     state = models.CharField(max_length=25, choices=STATE_TYPE, default="undone")
#     comments = models.JSONField(default=list)
#     priority = models.CharField(max_length=25, choices=PRIO_TYPE, default="low")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     due_date = models.DateTimeField()
#     reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='review_subtask')
#     completed_at = models.DateTimeField(null=True, blank=True)
#     subtasks = models.JSONField(default=list) 
#     log = models.JSONField(default=list, blank=True)
#     type = models.CharField(default="subtask")


class Comment(models.Model):
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE, related_name="task_comment")
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user_comment")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)