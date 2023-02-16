from django.urls import path
from . import views
##Urls
urlpatterns = [
    path('', views.apiFunctionOverview, name="apiFunctionOverview"),
    path('todo-list/', views.todoList, name="todo-list"),
    path('task-detail/<int:pk>/', views.taskDetail, name="task-Detail"),
    path('task-create/', views.taskCreate, name="task-Create"),
    path('task-update/<int:pk>/', views.taskUpdate, name="task-update"),
    path('task-status-update/<int:pk>/', views.UpdateStatus, name="task-status-update"),
    path('task-delete/<int:pk>/', views.taskDelete, name="task-delete"),

   ]