from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

from .forms import TodoForm

# Create your views here.

def Home(request):
    # return HttpResponse("Welcome to Todo Home Page!")
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todohome.html', context)

def TodoAdd(request):
    form = TodoForm(request.POST)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo')
        else:
            return HttpResponse("Invalid submission!")
    return render(request, 'todoadd.html', {'form': form})

def TodoDelete(request, pk):
    todo_to_delete = Todo.objects.get(id=pk)
    todo_to_delete.delete()
    return redirect('todohome')

def TodoEdit(request, pk):
    todo_edit = Todo.objects.get(id=pk)
    form = TodoForm(request.POST, instance=todo_edit)
    if form.is_valid():
        form.save()
        return redirect('todohome')
    context = {'form': form}
    return render(request, 'todoadd.html', context)
def TodoComplete(request, pk):
    form = Todo.objects.get(id=pk)
    form.completed = True
    form.save()
    return redirect('todohome')