from django.urls import path
from .views import CreateTaskView, TaskListView, SingleTaskView

urlpatterns = [
    path('tasks/', CreateTaskView.as_view(), name="task-create"),
    path('tasks/<int:customer_id>/', TaskListView.as_view(), name="task-list"),
    path('task/<int:pk>/', SingleTaskView.as_view(), name="task-detail" ),
]
