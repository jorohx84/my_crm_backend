from django.urls import path
from .views import CreateTaskView, TaskListView, SingleTaskView, CreateTaskCommentView, CommentUpdateView, SubtaskListView, SubtaskCountView, TaskBoardView

urlpatterns = [
    path('tasks/', CreateTaskView.as_view(), name="task-create"),
    path('tasks/<int:customer_id>/', TaskListView.as_view(), name="task-list"),
    path('task/<int:pk>/', SingleTaskView.as_view(), name="task-detail" ),
    path('comments/', CreateTaskCommentView.as_view(), name="comment-create"),
    path('comments/<int:pk>/', CommentUpdateView.as_view(), name="comment-detail"),
    # path('subtasks/', SubtaskCreatetView.as_view(), name="subtask-create"),
    path('subtasks/<int:parent_id>/', SubtaskListView.as_view(), name="subtask-list"),
    path('subtasks/count/<int:pk>/', SubtaskCountView.as_view(), name="subtask-count"),
    path('board/<int:pk>/', TaskBoardView.as_view(), name="board"),
]
