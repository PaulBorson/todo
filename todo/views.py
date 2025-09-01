from django.shortcuts import render,redirect
from .models import  Task

def index(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        new_Task = request.POST.get("task")

        if new_Task:
            Task.objects.create(title=new_Task)
    return render(request , 'todo/index.html',{'tasks':tasks})


# todo/views.py

def delete_task(request, task_id):  # ✅ task_id নিতে হবে
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')


# todo/views.py

def complete_task(request, task_id):  # ✅ এখানে task_id নিতে হবে
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('/')



# Create your views here.
