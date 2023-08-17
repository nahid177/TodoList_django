
from django.shortcuts import render, redirect
from . forms import TaskForm
from . models import TaskModel

# Create your views here.


def home(request):
    return render(request, './home.html')





def addtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showtasks')
    else:
        form = TaskForm()
    return render(request, 'addtask.html', {'form' : form})







def showtasks(request):
    task = TaskModel.objects.filter(is_completed=False)
    return render(request, 'showtasks.html', {'task' : task})







def edittask(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('showtasks')
        
    return render(request, 'addtask.html', {'form' : form})






def deletetask(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('showtasks')





def completetask(request, id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('complete')
  
  
  
  
            
def completion(request):
    task = TaskModel.objects.filter(is_completed=True)
    return render(request, 'complete.html', {'task' : task})
    