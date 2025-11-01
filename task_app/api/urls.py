from django.urls import path
from .views import CreateTaskView, TaskListView, SingleTaskView, CreateCommentView, CommentUpdateView, SubtaskCreatetView

urlpatterns = [
    path('tasks/', CreateTaskView.as_view(), name="task-create"),
    path('tasks/<int:customer_id>/', TaskListView.as_view(), name="task-list"),
    path('task/<int:pk>/', SingleTaskView.as_view(), name="task-detail" ),
    path('comments/', CreateCommentView.as_view(), name="comment-create"),
    path('comments/<int:pk>/', CommentUpdateView.as_view(), name="comment-detail"),
    path('subtasks/', SubtaskCreatetView.as_view(), name="subtask-create"),
]
