from .models import Task
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import *

"============Api Functions Overview==========="
@api_view(['GET'])
def apiFunctionOverview(request):
    api_urls = {
        'Todo List' :'/todo-list/',
        'Todo Task Detail' :'/task-detail/<int:pk>/',
        'Todo Task Create' :'/task-create/',
        'Todo Task Update' :'/task-update/<int:pk>/',
        'Todo Task Status Update' :'/task-status-update/<int:pk>/',
        'Todo Task Delete' :'/task-delete/<int:pk>/',
       
    }
    return Response(api_urls)

#for listing the task
@api_view(['GET'])
def todoList(request):
    #get all data from task model
    tasks = Task.objects.all()
    serializer = TodoSerializer(tasks, many = True)
    return Response(serializer.data)

# to get detail of particular task by their id
@api_view(['GET'])
def taskDetail(request, pk):
    #getting data which matches the id
    tasks = Task.objects.get(id=pk)
    serializer = TodoSerializer(tasks, many = False)
    return Response(serializer.data)


# add task
@api_view(['POST'])
def taskCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# update task title
@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TodoSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete task
@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Task deleted successfully.")

#update task status
@api_view(['POST'])
def UpdateStatus(request,pk):
    task = Task.objects.get(id = pk)
    serializer = TaskStatusSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
