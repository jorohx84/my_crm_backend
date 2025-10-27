from django.urls import path
from .views import CreateTaskView, TaskListView

urlpatterns = [
    path('tasks/', CreateTaskView.as_view(), name="task-create"),
    path('tasks/<int:customer_id>/', TaskListView.as_view(), name="task-create"),
]
