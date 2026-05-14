from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.utils import timezone

# Create your views here.
def task_list(request):
    tasks=Task.objects.all()
    return render(request, 'todo/task_list.html',{'tasks':tasks})

def add_task(request):
    if request=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        if title:
            Task.objects.create(title=title,descritpion=description)
        return redirect('task_list')
    return render(request,'todo/add_task.html')

# def complete_task

