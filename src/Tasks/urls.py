from django.urls import path
from .views import list_tasks, CreateTaskView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', list_tasks, name='home'),
    path('create/', CreateTaskView.as_view(), name="create"),
    path('<int:pk>/detail/', TaskDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name="delete")
]
