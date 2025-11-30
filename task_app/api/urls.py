from django.urls import path
from .views import CreateTaskView, TaskListView, SingleTaskView, CreateTaskCommentView, CommentListView, CommentUpdateView, CreateTaskTemplateView, TaskBoardAssigneeView, TaskBoardReviewerView, TaskBoardRealesesView, CreateLogView, LogListView, TaskTemplateUpdateDeleteView

urlpatterns = [
    path('tasks/', CreateTaskView.as_view(), name="task-create"),
    path('tasks/<int:customer_id>/<str:filter>/', TaskListView.as_view(), name="task-list"),
    path('task/<int:pk>/', SingleTaskView.as_view(), name="task-detail" ),
    path('comment-create/', CreateTaskCommentView.as_view(), name="comment-create"),
    path('comments/<int:task_id>/', CommentListView.as_view(), name="comment-detail"),
    path('comment/<int:pk>/', CommentUpdateView.as_view(), name="comment-detail"),
    path('task/logs/',  CreateLogView.as_view(), name="logs"),
    path('task/logs/<int:task_id>', LogListView.as_view(), name="loglist"),
    # path('subtasks/', SubtaskCreatetView.as_view(), name="subtask-create"),
    # path('subtasks/<int:parent_id>/', SubtaskListView.as_view(), name="subtask-list"),
    # path('subtasks/count/<int:pk>/', SubtaskCountView.as_view(), name="subtask-count"),
    path('board/<int:user_id>/assigned/', TaskBoardAssigneeView.as_view(), name="board-assignee"),
    path('board/<int:user_id>/reviewed/', TaskBoardReviewerView.as_view(), name="board-reviewer"),
    path('board/<int:user_id>/releases/', TaskBoardRealesesView.as_view(), name="board-releases"),
    path('task/template/', CreateTaskTemplateView.as_view(), name="template-create" ),
    path('task/template/<int:pk>/', TaskTemplateUpdateDeleteView.as_view(), name="single-template" )
]
