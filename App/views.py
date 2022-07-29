from django.shortcuts import redirect, render
from .forms import TaskForm
from django.contrib import messages
from .models import Task
# Create your views here.


def AddShowTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success ! Task Created')
            form = TaskForm()
    else:
        form = TaskForm()
    data = Task.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'index.html', context)


def UpdateTask(request, id):
    if request.method == "POST":
        updatedate = Task.objects.get(pk=id)
        form = TaskForm(request.POST, instance=updatedate)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update Task !')
    else:
        updatedate = Task.objects.get(pk=id)
        form = TaskForm(instance=updatedate)
    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def DeleteTask(request, id):
    if request.method == "POST":
        deletedata = Task.objects.get(pk=id)
        deletedata.delete()
        return redirect('addshowtask')
    else:
        return render(request, 'index.html')
