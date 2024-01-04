from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .forms import TaskForm

def list_tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks':tasks
    }
    return render(request, 'Tasks/index.html', context)

class CreateTaskView(CreateView):
    model = Task
    fields = ('title', 'content', 'due_date', 'priority')
    template_name = 'Tasks/create.html'
    success_url = "/"
    
    def add_task(request):
        if request.method=="POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'Tasks/create.html', {'form':form})

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'Tasks/update.html'
    success_url = "/"


class TaskDetailView(DetailView):
    model = Task
    template_name = "Tasks/detail.html"

class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"
    template_name = "Tasks/delete.html"