from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

def home(request):

    # ADD TASK
    if request.method == "POST":
        title = request.POST['title']

        Task.objects.create(title=title)
        
        return redirect('/')

    # SHOW TASKS
    tasks = Task.objects.all()

    return render(request, 'home.html', {'tasks': tasks})


# DELETE TASK
def delete_task(request, id):
    task = Task.objects.get(id=id)

    task.delete()

    return redirect('/')


# EDIT TASK
def edit_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.title = request.POST['title']
        task.save()

        return redirect('/')

    return render(request, 'edit.html', {'task': task})
